def ex020():
    import random

    # Exercício 20
    # O mesmo professor do desafio anterior quer sortear
    # a ordem de apresentação de trabalhos dos alunos.
    # Faça um programa que leia o nome dos quatro
    # alunos e mostre a ordem sorteada.

    print("Alunos para o sorteio:")
    aluno1 = "Ana"
    aluno2 = "Bia"
    aluno3 = "João"
    aluno4 = "Tiago"

    # Exibindo os nomes dos alunos
    for i, aluno in enumerate([aluno1, aluno2, aluno3, aluno4], start=1):
        print(f"Aluno {i}: {aluno}")

    # Lendo os nomes dos alunos
    alunos = [aluno1, aluno2, aluno3, aluno4]

    # Embaralhando a lista de alunos
    random.shuffle(alunos)

    # Exibindo a ordem sorteada
    print("A ordem de apresentação dos alunos será:")
    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}º lugar: {aluno}")
