# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.
print("=== Desafio 13 ===")
print("=== Aumento de 15% ===")
salario = float(input("Digite o salário do funcionário: R$ "))  # nosec
aumento = salario * 0.15
salario_final = salario + aumento
print(f"O novo salário do funcionário com 15% de aumento é: R$ {salario_final:.2f}")
print("=== Fim do Desafio 13 ===")
# # Fim do desafio 13
