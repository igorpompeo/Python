def ex018():
    # Exercício 18
    # Faça um programa que leia um ângulo qualquer e mostre na
    # tela o valor do seno, cosseno e tangente desse ângulo.
    # Exemplo: Digite o ângulo: 30. O ângulo de 30 tem o seno de 0.5,
    # o cosseno de 0.866 e a tangente de 0.577.
    # Importando a biblioteca math para usar as funções trigonométricas

    import math
    import random

    # Lendo um ângulo do usuário
    print("Digite o ângulo: ")

    # Gerando um ângulo aleatório entre 0 e 360 graus
    angulo = random.randint(0, 360)  # nosec

    # Exibindo o ângulo gerado
    print(f"Você digitou: {angulo} graus")

    # Convertendo o ângulo de graus para radianos
    print("Convertendo para radianos...")

    # Convertendo o ângulo para radianos
    # Alternativa usando a função radians da biblioteca math
    # angulo_rad = math.radians(angulo)
    # Alternativa manual
    # angulo_rad = angulo * (math.pi / 180)

    # Usando a função radians da biblioteca math
    angulo_rad = math.radians(angulo)

    # Calculando o seno, cosseno e tangente do ângulo
    seno = math.sin(angulo_rad)  # Seno
    cosseno = math.cos(angulo_rad)  # Cosseno
    tangente = math.tan(angulo_rad)  # Tangente

    # Exibindo os resultados
    print(
        f"O ângulo de {angulo} tem o seno de {seno:.3f},"
        f"o cosseno de {cosseno:.3f} e a tangente de {tangente:.3f}."
    )
