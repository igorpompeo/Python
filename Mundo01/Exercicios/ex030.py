def ex030():
    # Exercício 30
    # Crie um programa que leia um número inteiro
    # e mostre na tela se ele é PAR ou ÍMPAR.

    from random import randint
    from time import sleep

    from colorama import Fore, Style
    from emoji import emojize

    n = randint(0, 100)  # nosec

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def par_ou_impar(n):
        if n % 2 == 0:
            return "PAR"
        else:
            return "ÍMPAR"

    def obter_modo(auto=False):
        if auto:
            return randint(0, 100)  # nosec
        else:
            while True:
                try:
                    n = int(
                        input(  # nosec
                            Fore.YELLOW + "Digite um número inteiro: " + Style.RESET_ALL
                        )
                    )
                    return n
                except ValueError:
                    print(
                        Fore.RED
                        + "❌ Entrada inválida. Tente novamente."
                        + Style.RESET_ALL
                    )

    separador()
    print(
        Fore.YELLOW
        + emojize("🤔 Vamos verificar se o número é PAR ou ÍMPAR!")
        + Style.RESET_ALL
    )
    separador()
    modo = True
    n = obter_modo(auto=modo)
    print(emojize(f"🔢 Você digitou: {n}!"))
    sleep(1)
    resultado = par_ou_impar(n)
    print(emojize(f"🔍 O número {n} é {Fore.GREEN + resultado + Style.RESET_ALL}!"))
    separador()
    print(emojize("👋 Até a próxima!"))
