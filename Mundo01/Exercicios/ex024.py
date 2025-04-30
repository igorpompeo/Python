def ex024():
    from random import choice

    # Exercício 24
    # Crie um programa que leia o nome de uma cidade
    # e diga se ela começa ou não com o nome "Santo".
    print("Digite o nome da cidade:")
    cidade = ["São Paulo", "Santo André", "Santos", "São José", "São Vicente"]
    cidade = choice(cidade)  # nosec
    print("Cidade digitada:", cidade)
    if cidade[:5].upper() == "SANTO":
        print("A cidade começa com 'Santo'.")
    else:
        print("A cidade não começa com 'Santo'.")
