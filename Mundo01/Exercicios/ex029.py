def ex029():
    # Exercício 29
    # Escreva um programa que leia a velocidade de um carro.
    # Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    # A multa vai custar R$7,00 por cada Km acima do limite.

    from random import randint

    from colorama import Fore, Style

    def obter_modo(auto=False):
        if auto:
            return randint(60, 120)  # nosec
        else:
            while True:
                try:
                    return int(
                        input("\U0001f697 Digite a velocidade do carro: ")
                    )  # nosec
                except ValueError:
                    print("❌ Entrada inválida. Tente novamente.")
                    return randint(60, 120)  # nosec

    modo_automatico = True  # Ative ou desative modo automático aqui

    def verificar_multa(velocidade):
        print(f"\U0001f697 A velocidade do carro é {velocidade}Km/h")
        if velocidade > 80:
            print("\U0001f3ce" + Fore.RED + " Você foi multado!" + Style.RESET_ALL)
            multa = (velocidade - 80) * 7
            print(Fore.RED + f"O valor da multa é R${multa:.2f}" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Você não foi multado!" + Style.RESET_ALL)
        print("👋 Tenha um bom dia!")

    vel = obter_modo(auto=modo_automatico)
    verificar_multa(vel)
