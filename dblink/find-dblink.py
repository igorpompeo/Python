import re
import os
import sys
import csv

def load_dblink_list(csv_path):
    dblink_usernames = set()

    # print(f"[DEBUG] Tentando abrir o arquivo CSV em: {csv_path}")
    
    if not os.path.exists(csv_path):
        print(f"[ERROR] Arquivo {csv_path} não encontrado!")
        sys.exit(1)

    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')  # Mude para ',' se necessário
            header = next(reader, None)  # Lê o cabeçalho
            # print(f"[DEBUG] Cabeçalho do CSV: {header}")  # Debug do cabeçalho

            for row in reader:
                # print(f"[DEBUG] Linha lida: {row}")  # Debug de cada linha
                if len(row) >= 1: # Alterado de ">= 3" para ">= 1"
                    dblink_usernames.add(row[0].strip()) # Alterado de row[2] para row[0]

    except Exception as e:
        print(f"[ERROR] Falha ao ler {csv_path}: {e}")
        sys.exit(1)

    # print(f"[DEBUG] DBLinks carregados FINAL: {dblink_usernames}")  # Debug do set final
    return dblink_usernames

def find_dblink_calls_in_file(file_path, dblink_usernames):
    """ Procura chamadas de DBLink (@ seguido por um username do CSV) em um arquivo SQL. """
    object_name = os.path.basename(file_path)
    found_dblink = False

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            in_block_comment = False  # Para rastrear comentários em bloco

            for line_number, line in enumerate(lines, start=1):
                stripped_line = line.strip()
                is_commented = False

                # Verifica se estamos dentro de um bloco de comentário /* ... */
                if "/*" in stripped_line:
                    in_block_comment = True
                if "*/" in stripped_line:
                    in_block_comment = False

                # Verifica se a linha contém um comentário -- ou faz parte de um bloco de comentário
                if stripped_line.startswith("--") or in_block_comment:
                    is_commented = True

                # Verifica se há uma chamada de DBLink válida com @ seguido de um dos usernames da lista
                match = re.search(r'@(\b[A-Za-z0-9_]+\b)', line)
                if match:
                    # print(f"[DEBUG] Possível DBLink encontrado: {match.group(1)}")
                    username = match.group(1)
                    if username.strip().upper() in {name.upper() for name in dblink_usernames}:
                        found_dblink = True
                        log_message = f"[LOG] {object_name} - Linha {line_number}: {line.strip()}"
                        if is_commented:
                            log_message += " [COMENTADO]"
                        print(log_message)
    except Exception as e:
        print(f"[ERROR] Falha ao ler {file_path}: {e}")

    # print(f"[DEBUG] Lendo linha {line_number}: {line.strip()}")
    
    return found_dblink

def scan_files_from_list(file_list_path, dblink_usernames):
    """ Lê a lista de arquivos SQL do db_files.sql e verifica chamadas de DBLink. """
    found_any_dblink = False
    if not os.path.exists(file_list_path):
        print(f"[ERROR] Arquivo {file_list_path} não encontrado!")
        sys.exit(1)

    try:
        with open(file_list_path, 'r', encoding='utf-8') as file:
            files = file.read().splitlines() # Lê todas as linhas corretamente, sem pular a primeira
        
        # Remover linhas vazias ou que não terminam com ".sql"
        files = [line.strip() for line in files if line.strip() and line.endswith(".sql")]

        # print(f"[DEBUG] Arquivos SQL encontrados no db_files.sql:")
        # for idx, file in enumerate(files, start=1):
            # print(f"[DEBUG] {idx}. {file}")

        print(f"[INFO] Total de arquivos SQL listados: {len(files)}")

        for file_path in files:
            # print(f"[DEBUG] Verificando arquivo: {file_path}")

            if os.path.exists(file_path):
                if find_dblink_calls_in_file(file_path, dblink_usernames):
                    found_any_dblink = True
            else:
                print(f"[WARNING] Arquivo não encontrado: {file_path}")
    except Exception as e:
        print(f"[ERROR] Falha ao ler {file_list_path}: {e}")
        sys.exit(1)
    
    if found_any_dblink:
        print("[ERROR] Foram encontradas chamadas de DBLink. Falhando o pipeline.")
        # sys.exit(1)
    else:
        print("[INFO] Nenhum DBLink encontrado. Pipeline continua normalmente.")

if __name__ == "__main__":
    # Diretório base (garante que o script sempre ache os arquivos)
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Garante o caminho correto

    # Caminhos para os arquivos necessários
    DB_FILES_PATH = "./db_files.sql"
    DBLINK_LIST_PATH = os.path.join(BASE_DIR, "dblink_list.csv")

    print(f"[INFO] Lendo DBLinks de: {DBLINK_LIST_PATH}")
    dblink_usernames = load_dblink_list(DBLINK_LIST_PATH)

    # print(f"[DEBUG] DBLinks carregados: {dblink_usernames}")
    
    print(f"[INFO] Iniciando varredura em arquivos listados em: {DB_FILES_PATH}")
    scan_files_from_list(DB_FILES_PATH, dblink_usernames)
