def ex002():
    import random

    nomes = ["Lucas", "Ana", "Pedro", "Maria", "João"]

    print("Digite seu nome: ")

    print(f"É um prazer te conhecer, {random.choice(nomes)}!")  # nosec
