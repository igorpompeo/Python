def ex025():
    from random import choice

    # Exercício 25
    # Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
    # Solicita o nome da pessoa
    print("Digite seu nome:")

    # Cria nomes aleatórios
    nome = ["Ana Maria da Silva", "João da Silva", "Maria Clara", "Pedro Paulo"]

    # Escolhe um nome aleatório da lista
    nome = choice(nome)  # nosec

    # Exibe o nome escolhido
    print("Nome digitado:", nome)

    # Verifica se o nome contém "Silva"
    if "Silva" in nome:
        print("Seu nome tem 'Silva'.")
    else:
        print("Seu nome não tem 'Silva'.")
