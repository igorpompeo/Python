# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
import random
print('=== Desafio 08 ===')
print('Conversor de medidas')
# Gera um número aleatório de 1 a 10
n = random.uniform(1, 10)

# Faz os cálculos direto no print:
# cm = n * 100
# mm = n * 1000
print(f'{n:.1f} metros equivale a {(n*100):.1f} centímetros e {(n*1000):.1f} milímetros.')
print('=== Fim do Desafio 08 ===')
# Fim do desafio 08