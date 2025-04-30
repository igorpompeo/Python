import os

CAMINHO = os.path.join("Mundo01", "Exercicios")

for nome_arquivo in os.listdir(CAMINHO):
    if nome_arquivo.startswith("ex") and nome_arquivo.endswith(".py"):
        caminho_arquivo = os.path.join(CAMINHO, nome_arquivo)

        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()

        nome_funcao = nome_arquivo[:-3]  # ex001.py -> ex001

        # Se já tem uma função com esse nome, pula
        if f"def {nome_funcao}()" in conteudo:
            print(f"🔁 Já tem função em {nome_arquivo}, ignorando.")
            continue

        novo_conteudo = f"def {nome_funcao}():\n"
        for linha in conteudo.splitlines():
            novo_conteudo += f"    {linha}\n"

        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(novo_conteudo)

        print(f"✅ Atualizado: {nome_arquivo}")
