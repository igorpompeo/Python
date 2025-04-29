# menu.py
import os

while True:
    escolha = input("Digite o número do exercício (ex: 001), ou 'sair': ")
    if escolha == "sair":
        break

    caminho = os.path.join("Mundo01", "Exercicios", f"ex{escolha}.py")

    if os.path.exists(caminho):
        exec(open(caminho, encoding="utf-8").read())
    else:
        print("Arquivo não encontrado.")
