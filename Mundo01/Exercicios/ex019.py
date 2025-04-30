def ex019():
    import random

    # Exercício 19
    # Um professor quer sortear um dos seus quatro
    # alunos para apagar o quadro.
    # Faça um programa que ajude ele, lendo o nome dos
    # quatro alunos e escrevendo na tela o nome do escolhido.
    # Exemplo: Aluno 1: Ana. Aluno 2: Bia. Aluno 3:
    # Carlos. Aluno 4: Daniel. O aluno escolhido foi Carlos.
    # Importando a biblioteca random para usar a função choice

    print("Alunos para o sorteio:")
    aluno1 = "Ana"
    aluno2 = "Bia"
    aluno3 = "João"
    aluno4 = "Tiago"

    # Exibindo os nomes dos alunos
    for i, aluno in enumerate([aluno1, aluno2, aluno3, aluno4], start=1):
        print(f"Aluno {i}: {aluno}")

    # Lendo os nomes dos alunos
    print("Escolhendo um aluno aleatoriamente...")

    # Criando uma lista com os nomes dos alunos
    alunos = [aluno1, aluno2, aluno3, aluno4]

    # Escolhendo um aluno aleatoriamente
    escolhido = random.choice(alunos)  # nosec

    # Exibindo o nome do aluno escolhido
    print(f"O aluno escolhido foi: {escolhido}.")
