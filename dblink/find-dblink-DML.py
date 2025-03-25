import re
import os
import sys
import csv
import glob

def load_dblink_list(csv_path):
    dblink_usernames = set()
    
    if not os.path.exists(csv_path):
        print(f"[ERROR] Arquivo {csv_path} não encontrado!")
        sys.exit(1)

    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')  # Mude para ',' se necessário
            header = next(reader, None)  # Lê o cabeçalho

            for row in reader:
                if len(row) >= 1:
                    dblink_usernames.add(row[0].strip())

    except Exception as e:
        print(f"[ERROR] Falha ao ler {csv_path}: {e}")
        sys.exit(1)

    return dblink_usernames

def find_dblink_calls_in_file(file_path, dblink_usernames):
    """ Procura chamadas de DBLink (@ seguido por um username do CSV) em um arquivo SQL. """
    object_name = os.path.basename(file_path)
    found_dblink = False

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            in_block_comment = False  

            for line_number, line in enumerate(lines, start=1):
                stripped_line = line.strip()
                is_commented = False

                if "/*" in stripped_line:
                    in_block_comment = True
                if "*/" in stripped_line:
                    in_block_comment = False

                if stripped_line.startswith("--") or in_block_comment:
                    is_commented = True

                match = re.search(r'@(\b[A-Za-z0-9_]+\b)', line)
                if match:
                    username = match.group(1)
                    if username.strip().upper() in {name.upper() for name in dblink_usernames}:
                        found_dblink = True
                        log_message = f"[LOG] {object_name} - Linha {line_number}: {line.strip()}"
                        if is_commented:
                            log_message += " [COMENTADO]"
                        print(log_message)
    except Exception as e:
        print(f"[ERROR] Falha ao ler {file_path}: {e}")
    
    return found_dblink

def scan_files_from_list(file_list_path, dblink_usernames):
    """ Lê a lista de arquivos SQL do db_files.sql e verifica chamadas de DBLink. """
    found_any_dblink = False
    if not os.path.exists(file_list_path):
        print(f"[ERROR] Arquivo {file_list_path} não encontrado!")
        sys.exit(1)
