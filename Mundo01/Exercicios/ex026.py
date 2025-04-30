def ex026():
    # Exercício 26
    # Faça um programa que leia uma frase pelo teclado e mostre:
    # 1. Quantas vezes aparece a letra "A".
    # 2. Em que posição ela aparece a primeira vez.
    # 3. Em que posição ela aparece a última vez.
    frase = """Um Anel para todos governar, um Anel para encontrá-los,
    um Anel para a todos trazer e na escuridão aprisioná-los"""
    letra = frase.count("a") + frase.count("A")
    print("A letra 'A' aparece", letra, "vezes na frase.")
    print(
        "A letra 'A' aparece pela primeira vez na posição", frase.lower().find("a") + 1
    )
    print(
        "A letra 'A' aparece pela última vez na posição", frase.lower().rfind("a") + 1
    )
