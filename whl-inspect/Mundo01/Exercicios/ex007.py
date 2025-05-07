def ex007():
    # Desenvolva um programa que leia duas notas
    # de um aluno, calcule e mostre a média.
    import random

    print("=== Desafio 07 ===")
    print("Média de notas")

    # Gera um número aleatório de 1 a 100
    n1, n2 = random.uniform(1, 10), random.uniform(1, 10)  # nosec

    # Faz os cálculos direto no print:
    # - Média: (n1+n2)/2
    print(f"A média entre {n1:.2f} e " f"{n2:.2f} é igual a " f"{((n1 + n2) / 2):.2f}")
    print("=== Fim do Desafio 07 ===")
    # Fim do desafio 07
