def ex009():
    import random

    # Faça um programa que leia um número
    # inteiro e mostre na tela sua tabuada.
    print("=== Desafio 09 ===")
    print("Tabuada")

    # Gera um número aleatório de 1 a 100
    n = random.randint(1, 100)  # nosec
    print("-" * 20)
    print(f"A tabuada de {n} é:")

    for i in range(1, 11):
        print(f"{n:2} x {i:2} = {n * i}")

    print("-" * 20)
    print("=== Fim do Desafio 09 ===")
    # Fim do desafio 09
