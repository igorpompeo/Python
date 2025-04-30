import random

# Crie um script Python que leia o
# dia o mês e o ano de
# nascimento de uma pessoa e mostre
# uma mensagem a data formatada

dia = random.randint(1, 31)  # nosec
mes = random.randint(1, 12)  # nosec
ano = random.randint(1900, 2023)  # nosec
print(f"Você nasceu no dia {dia} de {mes} de {ano}. Correto?")
