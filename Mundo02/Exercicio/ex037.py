def ex037():
    # Escreva um programa que leia um número inteiro qualquer
    # e peça para o usuário escolher qual será a base de conversão:
    # 1- binário 2- octal 3- hexadecimal

    from random import randint

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return randint(1, 100), randint(1, 3)  # nosec
        else:
            while True:
                try:
                    numero = int(input("Digite um número inteiro: "))
                    print("Escolha a base de conversão:")
                    print("1 - Binário\n2 - Octal\n3 - Hexadecimal")
                    base = int(input("Sua escolha: "))
                    if base not in [1, 2, 3]:
                        raise ValueError
                    return numero, base
                except ValueError:
                    print(
                        Fore.RED
                        + "❌ Entrada inválida. Tente novamente."
                        + Style.RESET_ALL
                    )

    def conversao_base(numero, base):
        print(Fore.YELLOW + emojize("🔢 Conversão de Base Numérica"))
        print(Fore.YELLOW + emojize(f"🔢 Número: {numero}"))
        print(Fore.YELLOW + emojize(f"🔢 Base escolhida: {base}"))
        if base == 1:
            return bin(numero)[2:]
        elif base == 2:
            return oct(numero)[2:]
        elif base == 3:
            return hex(numero)[2:]
        else:
            raise ValueError("Base inválida.")

    separador()
    modo = obter_modo(auto=True)
    numero, base = modo
    resultado = conversao_base(numero, base)
    print(Fore.GREEN + emojize(f"📤 Resultado da conversão: {resultado}"))
    separador()
    print(Fore.YELLOW + emojize("👋 Até a próxima!") + Style.RESET_ALL)


ex037()
