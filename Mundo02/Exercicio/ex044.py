def ex044():
    # Elabore um programa que calcule o valor a ser pago por um produto,
    # considerando o seu preço normal e condição de pagamento:
    # - À vista dinheiro/cheque: 10% de desconto
    # - À vista no cartão: 5% de desconto
    # - Em até 2x no cartão: preço normal
    # - 3x ou mais no cartão: 20% de juros

    from random import randint, uniform

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return uniform(1, 1000), randint(1, 10)
        else:
            while True:
                try:
                    preco = float(input("Digite o preço do produto: "))
                    parcelas = int(input("Digite o número de parcelas: "))
                    if preco <= 0 or parcelas <= 0:
                        raise ValueError
                    return preco, parcelas
                except ValueError:
                    error_msg = Fore.RED + "❌ Entrada inválida. Tente novamente."
                    print(error_msg + Style.RESET_ALL)

    def calcular_preco_final(preco, parcelas):
        if parcelas == 1:  # À vista dinheiro/cheque
            return preco * 0.9
        elif parcelas == 2:  # À vista no cartão
            return preco * 0.95
        elif parcelas <= 2:  # Em até 2x no cartão
            return preco
        else:  # 3x ou mais no cartão
            return preco * 1.2

    def obter_condicao_pagamento(parcelas):
        condicoes = {
            1: "À vista dinheiro/cheque: 10% de desconto",
            2: "À vista no cartão: 5% de desconto",
        }
        if parcelas <= 2:
            return condicoes.get(parcelas, "Em até 2x no cartão: preço normal")
        return "3x ou mais no cartão: 20% de juros"

    separador()
    titulo = Fore.YELLOW + emojize("🧾 Simulador de Pagamento")
    print(titulo + Style.RESET_ALL)
    separador()

    preco, parcelas = obter_modo(auto=True)
    preco_final = calcular_preco_final(preco, parcelas)
    condicao = obter_condicao_pagamento(parcelas)

    resultado = Fore.GREEN + emojize(f"💰 Preço final: R${preco_final:.2f}")
    print(resultado)

    condicao_msg = Fore.BLUE + emojize(f"📌 Condição: {condicao}")
    print(condicao_msg + Style.RESET_ALL)

    separador()
    despedida = Fore.YELLOW + emojize("👋 Até a próxima!")
    print(despedida + Style.RESET_ALL)


ex044()
