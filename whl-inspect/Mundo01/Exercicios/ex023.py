def ex023():
    from random import randint

    # Exercício 23
    # Faça um programa que leia u número de 0 a 9999 e
    # mostre na tela cada um dos dígitos separados.
    # Exemplo: Digite um número: 1834. Unidade: 4. Dezena: 3. Centena: 8. Milhar: 1.

    n = randint(0, 9999)  # nosec

    print("Número digitado:", n)

    print("Unidade:", n // 1 % 10)

    print("Dezena:", n // 10 % 10)

    print("Centena:", n // 100 % 10)

    print("Milhar:", n // 1000 % 10)
