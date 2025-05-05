def ex031():
    # Exercício 31
    # Desenvolva um programa que pergunte a distância de uma viagem em km.
    # Calcule o preço da passagem, cobrando R$0,50 por km para viagens de
    # até 200km e R$0,45 para viagens mais longas.

    from random import randint
    from time import sleep

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return randint(1, 1000)  # nosec
        else:
            while True:
                try:
                    n = int(
                        input(  # nosec
                            Fore.YELLOW
                            + emojize(":airplane: Digite a distância da viagem em km: ")
                            + Style.RESET_ALL
                        )
                    )
                    if n > 0:
                        return n
                    else:
                        print(
                            Fore.RED
                            + "❌ Distância inválida. Tente novamente."
                            + Style.RESET_ALL
                        )
                except ValueError:
                    print(
                        Fore.RED
                        + "❌ Entrada inválida. Tente novamente."
                        + Style.RESET_ALL
                    )

    separador()
    print(
        Fore.YELLOW
        + emojize(":abacus: Vamos calcular o preço da passagem!")
        + Style.RESET_ALL
    )
    separador()
    modo = True
    distancia = obter_modo(auto=modo)
    print(
        Fore.YELLOW
        + emojize(f"🔍 A distância da viagem é {distancia} km!")
        + Style.RESET_ALL
    )
    sleep(1)
    if distancia <= 200:
        preco = distancia * 0.50
        print(
            Fore.GREEN
            + emojize(
                f"💰 O preço da passagem é R${preco:.2f} para viagens de até 200 km!"
            )
            + Style.RESET_ALL
        )
    else:
        preco = distancia * 0.45
        print(
            Fore.GREEN
            + emojize(
                f"💰 O preço da passagem é R${preco:.2f} para viagens acima de 200 km!"
            )
            + Style.RESET_ALL
        )
    separador()
    print(Fore.YELLOW + emojize("👋 Até a próxima!") + Style.RESET_ALL)
