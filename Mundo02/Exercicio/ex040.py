def ex040():
    # Crie um programa que leia duas notas de um aluno e calcule a média,
    # mostrando uma mensagem no final, de acordo com a média atingida:
    # - Média abaixo de 5.0: REPROVADO
    # - Média entre 5.0 e 6.9: RECUPERAÇÃO
    # - Média 7.0 ou superior: APROVADO

    from random import uniform

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return uniform(0, 10), uniform(0, 10)
        else:
            while True:
                try:
                    nota1 = float(input("Digite a primeira nota: "))
                    nota2 = float(input("Digite a segunda nota: "))
                    if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
                        raise ValueError
                    return nota1, nota2
                except ValueError:
                    print(
                        Fore.RED
                        + "❌ Entrada inválida. Tente novamente."
                        + Style.RESET_ALL
                    )

    def calcular_media(nota1, nota2):
        return (nota1 + nota2) / 2

    def verificar_situacao(media):
        if media < 5.0:
            return "REPROVADO"
        elif 5.0 <= media < 7.0:
            return "RECUPERAÇÃO"
        else:
            return "APROVADO"

    separador()
    print(Fore.YELLOW + "Simulador de Notas" + Style.RESET_ALL)
    separador()
    modo = obter_modo(auto=True)
    nota1, nota2 = modo
    media = calcular_media(nota1, nota2)
    situacao = verificar_situacao(media)
    print(Fore.GREEN + emojize(f"📤 Média: {media:.2f} - Situação: {situacao}"))
    separador()
    print(Fore.YELLOW + emojize("👋 Até a próxima!") + Style.RESET_ALL)


ex040()
