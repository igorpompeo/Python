def ex012():
    import random

    # Faça um algoritmo que leia o preço de um produto
    # e mostre seu novo preço, com 5% de desconto.

    print("=== Desafio 12 ===")
    print("=== Desconto de 5% ===")

    # Gera um número aleatório de 1 a 100
    preco = random.uniform(1, 100)  # nosec

    desconto = preco * 0.05
    preco_final = preco - desconto

    print(f"O preço do produto com 5% de " f"desconto é: R$ {(preco_final):.2f}")
    print("=== Fim do Desafio 12 ===")
    # Fim do desafio 12
