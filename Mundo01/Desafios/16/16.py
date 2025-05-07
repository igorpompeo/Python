# Exercicio 16
# Crie um programa que leia um numero Real qualquer
# pelo teclado e mostre na tela a sua porção inteira.
# Exemplo: Digite um numero: 6.127. O numero 6.127
# tem a parte inteira 6.
# Importando a biblioteca math para usar a função floor

import math
import random

# Lendo um numero real do usuário
print("Digite um numero: ")

# Gerando um numero real aleatório entre 0 e 100
num = random.random() * 100  # nosec

# Usando a função floor para obter a parte inteira do numero
parte_inteira = math.floor(num)

# Exibindo o resultado
print(f"O numero {num:.3f} tem a parte inteira {parte_inteira}.")

# Alternativa sem usar a biblioteca math
# num = float(input('Digite um numero: '))  # nosec
# Converte o numero para inteiro, descartando a parte decimal
# parte_inteira = int(num)
# print(f'O numero {num} tem a parte inteira {parte_inteira}.')
