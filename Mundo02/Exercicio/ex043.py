def ex043():
    # Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
    # calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
    # - Abaixo de 18.5: Abaixo do Peso
    # - Entre 18.5 e 25: Peso Ideal
    # - Entre 25 e 30: Sobrepeso
    # - Entre 30 e 40: Obesidade
    # - Acima de 40: Obesidade Mórbida

    from random import uniform

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return uniform(1.5, 2.0), uniform(50, 100)
        else:
            while True:
                try:
                    altura = float(input("Digite sua altura (em metros): "))
                    peso = float(input("Digite seu peso (em kg): "))
                    if altura <= 0 or peso <= 0:
                        raise ValueError
                    return altura, peso
                except ValueError:
                    print(
                        Fore.RED
                        + "❌ Entrada inválida. Tente novamente."
                        + Style.RESET_ALL
                    )

    def calcular_imc(altura, peso):
        return peso / (altura**2)

    def verificar_situacao(imc):
        if imc < 18.5:
            return "Abaixo do Peso"
        elif 18.5 <= imc < 25:
            return "Peso Ideal"
        elif 25 <= imc < 30:
            return "Sobrepeso"
        elif 30 <= imc < 40:
            return "Obesidade"
        else:
            return "Obesidade Mórbida"

    separador()
    print(Fore.YELLOW + "Simulador de IMC" + Style.RESET_ALL)
    separador()
    altura, peso = obter_modo(auto=True)
    imc = calcular_imc(altura, peso)
    situacao = verificar_situacao(imc)
    print(Fore.GREEN + emojize(f"📏 IMC: {imc:.2f} - Situação: {situacao}"))
    separador()
    print(Fore.YELLOW + emojize("👋 Até a próxima!") + Style.RESET_ALL)


ex043()
