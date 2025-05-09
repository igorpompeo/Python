def ex041():
    # A Confederação Nacional de Natação precisa de um algoritmo que
    # leia o ano de nascimento de um atleta e mostre sua categoria,
    # de acordo com a idade:
    # - Até 9 anos: MIRIM
    # - Até 14 anos: INFANTIL
    # - Até 19 anos: JÚNIOR
    # - Até 25 anos: SÊNIOR
    # - Acima de 25 anos: MASTER

    from datetime import datetime
    from random import randint

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_ano_nascimento(auto=False):
        if auto:
            return datetime.now().year - randint(1, 30)
        else:
            while True:
                try:
                    ano_nascimento = int(input("Digite o ano de nascimento: "))
                    if ano_nascimento < 1900 or ano_nascimento > datetime.now().year:
                        raise ValueError
                    return ano_nascimento
                except ValueError:
                    print(
                        Fore.RED
                        + "❌ Entrada inválida. Tente novamente."
                        + Style.RESET_ALL
                    )

    def calcular_idade(ano_nascimento):
        return datetime.now().year - ano_nascimento

    def verificar_categoria(idade):
        if idade <= 9:
            return "MIRIM"
        elif idade <= 14:
            return "INFANTIL"
        elif idade <= 19:
            return "JÚNIOR"
        elif idade <= 25:
            return "SÊNIOR"
        else:
            return "MASTER"

    separador()
    print(Fore.YELLOW + "Simulador de Categoria de Natação" + Style.RESET_ALL)
    separador()
    ano_nascimento = obter_ano_nascimento(auto=True)
    idade = calcular_idade(ano_nascimento)
    categoria = verificar_categoria(idade)
    print(Fore.GREEN + emojize(f"🏊 Idade: {idade} anos - Categoria: {categoria}"))
    separador()
    print(Fore.YELLOW + emojize("👋 Até a próxima!") + Style.RESET_ALL)


ex041()
