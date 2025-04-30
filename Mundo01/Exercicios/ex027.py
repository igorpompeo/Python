def ex027():
    # Exercício 27
    # Faça um programa que leia o nome completo de uma pessoa,
    # mostrando em seguida o primeiro e o último nome separadamente.
    nome_completo = "Igor Pompeo Tavares de Souza"
    print("Nome completo:", nome_completo)
    nome = nome_completo.split()
    print("Primeiro nome:", nome[0])
    print("Último nome:", nome[-1])
