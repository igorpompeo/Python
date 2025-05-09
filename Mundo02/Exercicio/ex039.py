def ex039():
    # Faça um programa que leia o ano de nascimento de um
    # jovem e informe, de acordo com a sua idade:
    # - Se ele ainda vai se alistar ao serviço militar.
    # - Se é hora de se alistar.
    # - Se já passou do tempo de alistamento.
    # Seu programa também deverá mostrar o tempo que falta ou que
    # passou do prazo para o alistamento.

    from datetime import datetime
    from random import randint

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return randint(1900, 2023)
        else:
            while True:
                try:
                    ano_nascimento = int(input("Ano de nascimento: "))
                    if ano_nascimento < 1900 or ano_nascimento > datetime.now().year:
                        raise ValueError
                    return ano_nascimento
                except ValueError:
                    error_msg = Fore.RED + "❌ Entrada inválida. Tente novamente."
                    print(error_msg + Style.RESET_ALL)

    def calcular_idade(ano_nascimento):
        ano_atual = datetime.now().year
        return ano_atual - ano_nascimento

    def verificar_alistamento(idade):
        if idade < 18:
            return f"Faltam {18 - idade} anos para o alistamento."
        elif idade == 18:
            return "É hora de se alistar!"
        else:
            return f"Já passou {idade - 18} anos do prazo para o alistamento."

    separador()
    titulo = Fore.YELLOW + "Simulador de Alistamento Militar"
    print(titulo + Style.RESET_ALL)
    separador()
    modo = obter_modo(auto=True)
    ano_nascimento = modo
    idade = calcular_idade(ano_nascimento)
    resultado = verificar_alistamento(idade)
    resultado_msg = Fore.GREEN + emojize(f"📤 Resultado: {resultado}")
    print(resultado_msg)
    separador()
    despedida = Fore.YELLOW + emojize("👋 Até a próxima!")
    print(despedida + Style.RESET_ALL)


ex039()
