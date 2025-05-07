def ex017():
    # Exercício 17
    # Faça um programa que leia o comprimento do cateto
    # oposto e do cateto adjacente de um triângulo retângulo,
    # calcule e mostre o comprimento da hipotenusa.
    # Exemplo: Digite o comprimento do cateto oposto: 3.0.
    # Digite o comprimento do cateto adjacente: 4.0.
    # A hipotenusa é: 5.0.
    # Importando a biblioteca math para usar a função sqrt

    import math
    import random

    # Lendo os comprimentos dos catetos do usuário
    print("Digite o comprimento do cateto oposto: ")

    # Gerando um número real aleatório entre 0 e 10
    cateto_oposto = random.random() * 10  # nosec

    print(f"Você digitou: {cateto_oposto:.2f}")

    # Lendo o comprimento do cateto adjacente
    print("Digite o comprimento do cateto adjacente: ")

    # Gerando um número real aleatório entre 0 e 10
    cateto_adjacente = random.random() * 10  # nosec

    # Exibindo o valor do cateto adjacente
    print(f"Você digitou:  {cateto_adjacente:.2f}")

    # Calculando o comprimento da hipotenusa
    # usando o Teorema de Pitágoras
    hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

    # Exibindo o resultado
    print(f"A hipotenusa é: {hipotenusa:.2f}.")

    # Alternativa sem usar a biblioteca math
    # cateto_oposto = float(input('Digite o comprimento
    # do cateto oposto: '))  # nosec
    # cateto_adjacente = float(input('Digite o comprimento
    # do cateto adjacente: '))  # nosec
    # hipotenusa = (cateto_oposto**2 + cateto_adjacente**2)**0.5
    # # Calculando a hipotenusa manualmente
    # print(f'A hipotenusa é: {hipotenusa:.2f}.')
