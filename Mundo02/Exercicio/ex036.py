def ex036():
    # Escreva um programa para aprovar o emprestimo bancario para
    # a compra de uma casa. O programa vai perguntar o valor da casa,
    # o salario do comprador e em quantos anos ele vai pagar.
    # Calcule o valor da prestação mensal, sabendo que ele não pode
    # exceder 30% do salario ou entao o emprestimo sera negado.

    from random import randint, uniform

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return [
                uniform(100000, 500000),
                uniform(1000, 5000),
                randint(1, 30),
            ]  # nosec
        else:
            while True:
                try:
                    valor_casa = float(input("Valor da casa: R$"))
                    salario = float(input("Salário: R$"))
                    anos = int(input("Anos para pagar: "))
                    return [valor_casa, salario, anos]
                except ValueError:
                    print(
                        Fore.RED
                        + "❌ Entrada inválida. Tente novamente."
                        + Style.RESET_ALL
                    )

    def analisar_emprestimo(valor_casa, salario, anos):
        separador()
        print(Fore.YELLOW + emojize(f"🏠 Valor da casa: R${valor_casa:.2f}"))
        print(Fore.YELLOW + emojize(f"💰 Salário: R${salario:.2f}"))
        print(Fore.YELLOW + emojize(f"🗓️  Anos para pagar: {anos} anos"))
        separador()

        prestacao = valor_casa / (anos * 12)
        limite = salario * 0.3

        casa_msg = Fore.YELLOW + emojize(f"🏠 Valor da casa: R${valor_casa:.2f}")
        print(casa_msg)

        separador()

        if prestacao <= limite:
            print(Fore.GREEN + "✅ Empréstimo Aprovado!")
        else:
            print(Fore.RED + "❌ Empréstimo Negado!")

    separador()
    print(Fore.YELLOW + "Simulador de Empréstimo Bancário" + Style.RESET_ALL)
    separador()
    modo = obter_modo(auto=True)
    valor_casa, salario, anos = modo
    analisar_emprestimo(valor_casa, salario, anos)
    separador()
    print(Fore.YELLOW + emojize("👋 Até a próxima!") + Style.RESET_ALL)


ex036()
