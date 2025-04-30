def ex004():
    import random
    import string

    # Faça um programa que leia algo pelo teclado e mostre na
    # tela o seu tipo primitivo e todas as informações possíveis sobre ele.
    print("Digite algo:")
    n = "".join(random.choices(string.ascii_letters + string.digits, k=10))  # nosec
    print("O tipo primitivo desse valor é:", type(n))
    print("Só tem espaços?", n.isspace())
    print("É um número?", n.isnumeric())
    print("É alfabético?", n.isalpha())
    print("É alfanumérico?", n.isalnum())
    print("Está em maiúsculas?", n.isupper())
    print("Está em minúsculas?", n.islower())
    print("Está capitalizada?", n.istitle())
