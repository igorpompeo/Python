def ex010():
    import random

    # Crie um programa que leia quanto dinheiro uma pessoa
    # tem na carteira e mostre quantos dólares ela pode comprar.
    # Considere US$1,00 = R$3,27.

    print("=== Desafio 10 ===")
    print("=== Conversor de Reais para Dólares ===")

    # Gera um número aleatório de 1 a 100
    n = random.uniform(1, 100)  # nosec

    # # Faz os cálculos direto no print:
    # dolar = n / 3.27
    print(f"Com R$ {n:.2f} você pode comprar US$ {(n / 3.27):.2f}")

    print("=== Fim do Desafio 10 ===")
    # Fim do desafio 10
