def ex028():
    import os
    import platform
    from random import randint
    from time import sleep

    from colorama import Fore, Style

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_palpite(auto=False):
        if auto:
            return randint(0, 5)  # nosec
        else:
            while True:
                try:
                    n = int(
                        input(  # nosec
                            Fore.YELLOW
                            + "Digite um número entre 0 e 5: "
                            + Style.RESET_ALL
                        )
                    )
                    if 0 <= n <= 5:
                        return n
                    else:
                        print(Fore.RED + "Número fora do intervalo." + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + "Entrada inválida." + Style.RESET_ALL)

    def limpar_tela():
        if platform.system() == "Windows":
            os.system("cls")  # nosec B605 B607
        else:
            os.system("clear")  # nosec B605 B607

    # Ative ou desative modo automático aqui:
    modo_automatico = True

    limpar_tela()
    n = randint(0, 5)  # nosec

    separador()
    print(Fore.YELLOW + "Vou pensar em um número entre 0 e 5..." + Style.RESET_ALL)
    sleep(1)
    print(Fore.YELLOW + "Pensando..." + Style.RESET_ALL)
    sleep(2)
    separador()

    n1 = obter_palpite(auto=modo_automatico)

    print(Fore.YELLOW + f"Você escolheu o número {n1}!" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Eu escolhi o número {n}!" + Style.RESET_ALL)
    separador()

    if n1 == n:
        print(Fore.GREEN + "Você venceu!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Você perdeu!" + Style.RESET_ALL)

    separador()
    print(Fore.YELLOW + "Fui!" + Style.RESET_ALL)
    separador()
