def ex011():
    import random

    # Faça um programa que leia a largura e a altura de uma parede em metros,
    # calcule a sua área e a quantidade de tinta necessária para pintá-la,
    # sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

    print("=== Desafio 11 ===")
    print("=== Pintura de Parede ===")

    # Gera um número aleatório de 1 a 100
    largura, altura = random.uniform(1, 100), random.uniform(1, 100)  # nosec

    # Faz os cálculos direto no print:
    # area = largura * altura
    # litros = area / 2
    print(
        f"A área da parede é {(largura * altura):.2f} m² "
        f"e você precisará de {((largura * altura) / 2):.2f} "
        f"litros de tinta para pintá-la."
    )
    print("=== Fim do Desafio 11 ===")
    # Fim do desafio 11
