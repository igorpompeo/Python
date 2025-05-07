def ex022():
    # Exercício 22
    # Crie um programa que leia o nome completo de uma pessoa e mostre:
    # 1. O nome com todas as letras maiúsculas e minúsculas.
    # 2. Quantas letras ao todo (sem considerar espaços).
    # 3. Quantas letras tem o primeiro nome.
    print("Nome completo:")

    nome = "Ana Maria da Silva"

    print("Nome:", nome)

    print("Seu nome em maiusculas:", nome.upper())

    print("Seu nome em minusculas:", nome.lower())

    print("Seu nome tem", len(nome) - nome.count(" "), "letras")

    print(
        "Seu primeiro nome é", nome.split()[0], "e tem", len(nome.split()[0]), "letras"
    )
