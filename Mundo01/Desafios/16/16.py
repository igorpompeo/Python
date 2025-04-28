# Exerc�cio 16
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Exemplo: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.
# Importando a biblioteca math para usar a função floor
import math, random
# Lendo um número real do usuário
print('Digite um número: ')
num = random.random() * 100  # Gerando um número real aleatório entre 0 e 100
# Usando a função floor para obter a parte inteira do número
parte_inteira = math.floor(num)
# Exibindo o resultado
print(f'O número {num:.3f} tem a parte inteira {parte_inteira}.')
# Alternativa sem usar a biblioteca math
# num = float(input('Digite um número: '))
# parte_inteira = int(num)  # Converte o número para inteiro, descartando a parte decimal
# print(f'O número {num} tem a parte inteira {parte_inteira}.')