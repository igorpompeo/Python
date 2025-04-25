import os

dir_exercicios = os.path.join("Mundo01", "Exercicios")
arquivos = sorted(f for f in os.listdir(dir_exercicios) if f.startswith("ex") and f.endswith(".py"))

print(f"Executando {len(arquivos)} exercícios...\n")

for arquivo in arquivos:
    print(f"==> Rodando {arquivo}")
    caminho = os.path.join(dir_exercicios, arquivo)
    try:
        exec(open(caminho, encoding="utf-8").read())
    except Exception as e:
        print(f"Erro em {arquivo}: {e}")
    print("-" * 40)
