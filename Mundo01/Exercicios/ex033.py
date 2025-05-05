def ex033():
    # Exercício 33
    # Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

    from random import randint

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return [randint(0, 100) for _ in range(3)]  # nosec
        else:
            while True:
                try:
                    numeros = [
                        int(
                            input(  # nosec
                                Fore.YELLOW
                                + emojize(":one: Digite o primeiro número: ")
                                + Style.RESET_ALL
                            )
                        ),
                        int(
                            input(  # nosec
                                Fore.YELLOW
                                + emojize(":two: Digite o segundo número: ")
                                + Style.RESET_ALL
                            )
                        ),
                        int(
                            input(  # nosec
                                Fore.YELLOW
                                + emojize(":three: Digite o terceiro número: ")
                                + Style.RESET_ALL
                            )
                        ),
                    ]
                    return numeros
                except ValueError:
                    print(
                        Fore.RED
                        + "❌ Entrada inválida. Tente novamente."
                        + Style.RESET_ALL
                    )

    def analisar_numeros(numeros):
        separador()
        print(
            Fore.YELLOW
            + emojize(f'🔍 Números escolhidos: {", ".join(map(str, numeros))}')
            + Style.RESET_ALL
        )
        separador()

        if len(set(numeros)) == 1:
            print(
                Fore.GREEN
                + emojize("✅ Todos os números são iguais!")
                + Style.RESET_ALL
            )
        else:
            maior = max(numeros)
            menor = min(numeros)
            print(
                Fore.GREEN
                + emojize(f"✅ Maior número: {maior} | Menor número: {menor}")
                + Style.RESET_ALL
            )

    separador()
    print(
        Fore.YELLOW
        + emojize("🔢 Vamos descobrir o maior e o menor número!")
        + Style.RESET_ALL
    )
    separador()
    modo = True
    numeros = obter_modo(auto=modo)
    analisar_numeros(numeros)
    separador()
    print(Fore.YELLOW + emojize("👋 Até a próxima!") + Style.RESET_ALL)
