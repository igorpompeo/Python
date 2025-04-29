import os
import sys

dir_exercicios = os.path.join("Mundo01", "Exercicios")
arquivos = sorted(
    f for f in os.listdir(dir_exercicios) if f.startswith("ex") and f.endswith(".py")
)

print(f"Executando {len(arquivos)} exercícios...\n")

errors = 0
for arquivo in arquivos:
    print(f"==> Rodando {arquivo}")
    caminho = os.path.join(dir_exercicios, arquivo)
    try:
        exec(open(caminho, encoding="utf-8").read())
    except Exception as e:
        print(f"❌ Erro em {arquivo}: {e}")
        errors += 1
    print("-" * 40)

if errors:
    print(f"⚠️ {errors} erro(s) encontrado(s) nos exercícios.")
    sys.exit(1)
else:
    print("✅ Todos os exercícios rodaram sem erros.")
    sys.exit(0)
