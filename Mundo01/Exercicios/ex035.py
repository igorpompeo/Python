def ex035():
    # Exercício 35
    # Desenvolva um programa que leia o comprimento de três retas e diga
    # ao usuário se elas podem ou não formar um triângulo.

    from random import randint

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return [randint(1, 100) for _ in range(3)]  # nosec
        else:
            while True:
                try:
                    retas = [
                        float(
                            input(  # nosec
                                Fore.YELLOW
                                + emojize(
                                    ":straight_ruler: Digite o comprimento "
                                    "da primeira reta: "
                                )
                                + Style.RESET_ALL
                            )
                        ),
                        float(
                            input(  # nosec
                                Fore.YELLOW
                                + emojize(
                                    ":straight_ruler: Digite o comprimento "
                                    "da segunda reta: "
                                )
                                + Style.RESET_ALL
                            )
                        ),
                        float(
                            input(  # nosec
                                Fore.YELLOW
                                + emojize(
                                    ":straight_ruler: Digite o comprimento "
                                    "da terceira reta: "
                                )
                                + Style.RESET_ALL
                            )
                        ),
                    ]
                    return retas
                except ValueError:
                    print(
                        Fore.RED
                        + "❌ Entrada inválida. Tente novamente."
                        + Style.RESET_ALL
                    )

    def verificar_triangulo(retas):
        separador()
        print(
            Fore.YELLOW
            + emojize(f'🔍 Comprimentos das retas: {", ".join(map(str, retas))}')
            + Style.RESET_ALL
        )
        separador()

        a, b, c = sorted(retas)
        if a + b > c:
            print(
                Fore.GREEN
                + emojize("✅ As retas podem formar um triângulo!")
                + Style.RESET_ALL
            )
        else:
            print(
                Fore.RED
                + emojize("❌ As retas não podem formar um triângulo!")
                + Style.RESET_ALL
            )

    separador()
    print(
        Fore.YELLOW
        + emojize("🔺 Vamos verificar se as retas podem formar um triângulo!")
        + Style.RESET_ALL
    )
    separador()
    modo = True
    retas = obter_modo(auto=modo)
    verificar_triangulo(retas)
    separador()
    print(Fore.YELLOW + emojize("👋 Até a próxima!") + Style.RESET_ALL)
