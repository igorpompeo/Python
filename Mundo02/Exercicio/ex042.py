def ex042():
    # Refaça o exercício 35 dos triângulos, acrescentando o recurso
    # de mostrar que tipo de triângulo será formado:
    # - Equilátero: todos os lados iguais
    # - Isósceles: dois lados iguais
    # - Escaleno: todos os lados diferentes

    from random import randint

    from colorama import Fore, Style
    from emoji import emojize

    def separador():
        print(Fore.CYAN + "=-" * 20 + Style.RESET_ALL)

    def obter_modo(auto=False):
        if auto:
            return [randint(1, 100) for _ in range(3)]
        else:
            while True:
                try:
                    mensagem = Fore.YELLOW + emojize(":straight_ruler: Digite o ")
                    retas = [
                        float(input(mensagem + "comprimento da primeira reta: ")),
                        float(input(mensagem + "comprimento da segunda reta: ")),
                        float(input(mensagem + "comprimento da terceira reta: ")),
                    ]
                    return retas
                except ValueError:
                    erro = Fore.RED + "❌ Entrada inválida. Tente novamente."
                    print(erro + Style.RESET_ALL)

    def verificar_triangulo(retas):
        separador()
        comprimentos = Fore.YELLOW + emojize(
            f'🔍 Comprimentos das retas: {", ".join(map(str, retas))}'
        )
        print(comprimentos)

        a, b, c = retas
        forma_triangulo = (a + b > c) and (a + c > b) and (b + c > a)

        if forma_triangulo:
            if a == b == c:
                tipo = "Equilátero"
            elif a == b or a == c or b == c:
                tipo = "Isósceles"
            else:
                tipo = "Escaleno"
            resultado = Fore.GREEN + emojize(f"✅ É um triângulo {tipo}!")
        else:
            resultado = Fore.RED + emojize("❌ Não é um triângulo!")

        print(resultado)

    separador()
    titulo = Fore.YELLOW + emojize("🔺 Simulador de Triângulos")
    print(titulo + Style.RESET_ALL)
    separador()
    modo = obter_modo(auto=True)
    verificar_triangulo(modo)
    separador()
    despedida = Fore.YELLOW + emojize("👋 Até a próxima!")
    print(despedida + Style.RESET_ALL)


ex042()
