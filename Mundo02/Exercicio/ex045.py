def ex045():
    # Crie um programa que faça o computador jogar Jokenpô com você.

    from random import choice
    from time import sleep

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_jogada(auto=False):
        if auto:
            return choice(["pedra", "papel", "tesoura"])
        else:
            while True:
                try:
                    prompt = Fore.YELLOW + emojize(
                        ":hand: Escolha sua jogada " "(pedra, papel ou tesoura): "
                    )
                    jogada = input(prompt + Style.RESET_ALL).lower()

                    if jogada not in ["pedra", "papel", "tesoura"]:
                        raise ValueError
                    return jogada
                except ValueError:
                    error_msg = Fore.RED + "❌ Entrada inválida. Tente novamente."
                    print(error_msg + Style.RESET_ALL)

    def verificar_vencedor(jogada_usuario, jogada_computador):
        if jogada_usuario == jogada_computador:
            return "Empate"
        elif (
            (jogada_usuario == "pedra" and jogada_computador == "tesoura")
            or (jogada_usuario == "papel" and jogada_computador == "pedra")
            or (jogada_usuario == "tesoura" and jogada_computador == "papel")
        ):
            return "Você ganhou!"
        return "Computador ganhou!"

    def exibir_resultado(jogada_usuario, jogada_computador, resultado):
        print(Fore.YELLOW + emojize("🤖 Computador jogou: ") + jogada_computador)
        print(Fore.YELLOW + emojize("🧍 Você jogou: ") + jogada_usuario)
        print(Fore.GREEN + emojize(f"🏆 Resultado: {resultado}"))

    separador()
    titulo = Fore.YELLOW + emojize("✊🖐✌ Simulador de Jokenpô")
    print(titulo + Style.RESET_ALL)
    separador()

    jogada_usuario = obter_jogada(auto=True)
    jogada_computador = obter_jogada(auto=True)

    sleep(1)
    resultado = verificar_vencedor(jogada_usuario, jogada_computador)
    exibir_resultado(jogada_usuario, jogada_computador, resultado)

    separador()
    despedida = Fore.YELLOW + emojize("👋 Até a próxima!")
    print(despedida + Style.RESET_ALL)


ex045()
