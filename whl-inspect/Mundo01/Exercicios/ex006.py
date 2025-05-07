def ex006():
    import random

    # crie um algoritmo que leia um número
    # e mostre o seu dobro, triplo e raiz quadrada.

    print("=== Desafio 06 ===")

    # Gera um número aleatório de 1 a 100
    n = random.randint(1, 100)  # nosec

    # Faz os cálculos direto no print:
    # - Dobro: n*2
    # - Triplo: n*3
    # - Raiz quadrada: n**(1/2), formatado com 2 casas decimais
    print(
        f"O dobro de {n} é {n * 2}, o triplo é {n * 3} "
        f"e a raiz quadrada é {(n ** (1 / 2)):.2f}."
    )

    print("=== Fim do Desafio 06 ===")
    # Fim do desafio 06
