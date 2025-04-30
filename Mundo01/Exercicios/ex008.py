def ex008():
    # Escreva um programa que leia um valor em metros
    # e o exiba convertido em centímetros e milímetros.
    import random

    print("=== Desafio 08 ===")
    print("Conversor de medidas")
    # Gera um número aleatório de 1 a 10
    n = random.uniform(1, 10)  # nosec

    km = n / 1000
    hm = n / 100
    dam = n / 10
    dm = n * 10
    cm = n * 100
    mm = n * 1000

    print(
        f"{n:.1f} metros equivale a:\n{km:.1f} kilometros,\n"
        f"{hm:.1f} hectómetro,\n{dam:.1f} decâmetro,\n"
        f"{dm:.1f} decímetro,\n{cm:.1f} centímetros\n"
        f"e {mm:.1f} milímetros."
    )
    print("=== Fim do Desafio 08 ===")
    # Fim do desafio 08
