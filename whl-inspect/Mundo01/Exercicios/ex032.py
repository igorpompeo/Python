def ex032():
    # Exercício 32
    # Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

    from datetime import datetime

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return datetime.now().year
        else:
            while True:
                try:
                    n = int(
                        input(  # nosec
                            Fore.YELLOW
                            + emojize(
                                ":calendar: Digite um ano (ou 0 para o ano atual): "
                            )
                            + Style.RESET_ALL
                        )
                    )
                    return n
                except ValueError:
                    print(
                        Fore.RED
                        + "❌ Entrada inválida. Tente novamente."
                        + Style.RESET_ALL
                    )

    separador()
    print(
        Fore.YELLOW
        + emojize(":calendar: Vamos verificar se o ano é bissexto!")
        + Style.RESET_ALL
    )
    separador()
    modo = True
    ano = obter_modo(auto=modo)
    if ano == 0:
        ano = datetime.now().year
    print(Fore.YELLOW + emojize(f"🔍 O ano escolhido é {ano}!") + Style.RESET_ALL)
    separador()
    print(
        Fore.YELLOW + emojize("🔍 Verificando se o ano é bissexto...") + Style.RESET_ALL
    )
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(Fore.GREEN + emojize(f"✅ O ano {ano} é bissexto!") + Style.RESET_ALL)
    else:
        print(Fore.RED + emojize(f"❌ O ano {ano} não é bissexto!") + Style.RESET_ALL)
    separador()
    print(Fore.YELLOW + emojize("👋 Até a próxima!") + Style.RESET_ALL)
