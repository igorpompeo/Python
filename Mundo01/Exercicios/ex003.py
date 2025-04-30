def ex003():
    # Crie um script Python que leia
    # dois números e tente mostrar a soma entre eles.
    import random

    n1, n2 = random.randint(1, 100), random.randint(1, 100)  # nosec
    print(f"A soma entre {n1} e {n2} é {n1 + n2}")
