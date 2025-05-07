def ex034():
    # Exercício 34
    # Escreva um programa que pergunte o salário de um funcionário
    # e calcule o valor do seu aumento.
    # Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
    # Para os inferiores ou iguais, o aumento é de 15%.

    from random import random

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return round(random() * 4000, 2)  # nosec B311
        else:
            while True:
                try:
                    n = float(
                        input(  # nosec
                            Fore.YELLOW
                            + emojize(":moneybag: Digite o salário do funcionário: ")
                            + Style.RESET_ALL
                        )
                    )
                    if n >= 0:
                        return n
                    else:
                        print(
                            Fore.RED
                            + "❌ Salário inválido. Tente novamente."
                            + Style.RESET_ALL
                        )
                except ValueError:
                    print(
                        Fore.RED
                        + "❌ Entrada inválida. Tente novamente."
                        + Style.RESET_ALL
                    )

    def calcular_aumento(salario):
        percentual = 0.10 if salario > 1250 else 0.15
        aumento = salario * percentual
        novo_salario = salario + aumento
        return aumento, novo_salario, percentual

    separador()
    print(
        Fore.YELLOW
        + emojize("💼 Vamos calcular o aumento do salário!")
        + Style.RESET_ALL
    )
    separador()
    modo = True
    salario = obter_modo(auto=modo)

    print(
        Fore.YELLOW
        + emojize(f"🔍 O salário informado é R${salario:.2f}!")
        + Style.RESET_ALL
    )
    separador()

    print(Fore.YELLOW + emojize("🔍 Calculando o aumento...") + Style.RESET_ALL)
    aumento, novo_salario, percentual = calcular_aumento(salario)

    print(
        Fore.GREEN
        + emojize(f"✅ Aumento de {int(percentual*100)}%: R${aumento:.2f}")
        + Style.RESET_ALL
    )
    print(
        Fore.YELLOW
        + emojize(f"💰 Novo salário: R${novo_salario:.2f}")
        + Style.RESET_ALL
    )
    separador()
    print(Fore.YELLOW + emojize("👋 Até a próxima!") + Style.RESET_ALL)
