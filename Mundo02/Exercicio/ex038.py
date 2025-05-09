def ex037():
    # Escreva um programa que leia dois números inteiros
    # e compare-os, mostrando na tela uma mensagem:
    # - O primeiro valor é maior
    # - O segundo valor é maior
    # - Não existe valor maior, os dois são iguais

    from random import randint

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return randint(1, 100), randint(1, 100)
        else:
            while True:
                try:
                    num1 = int(input("Digite o primeiro número: "))
                    num2 = int(input("Digite o segundo número: "))
                    return num1, num2
                except ValueError:
                    print(
                        Fore.RED
                        + "❌ Entrada inválida. Tente novamente."
                        + Style.RESET_ALL
                    )

    def comparar_numeros(num1, num2):
        print(Fore.YELLOW + emojize("🔢 Comparação de Números"))
        print(Fore.YELLOW + emojize(f"🔢 Primeiro número: {num1}"))
        print(Fore.YELLOW + emojize(f"🔢 Segundo número: {num2}"))

        if num1 > num2:
            return "O primeiro valor é maior."
        elif num2 > num1:
            return "O segundo valor é maior."
        else:
            return "Não existe valor maior, os dois são iguais."

    separador()
    modo = obter_modo(auto=True)
    num1, num2 = modo
    resultado = comparar_numeros(num1, num2)
    print(Fore.GREEN + emojize(f"📤 Resultado: {resultado}"))
    separador()
    print(Fore.YELLOW + emojize("👋 Até a próxima!") + Style.RESET_ALL)


ex037()
