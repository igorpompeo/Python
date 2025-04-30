def ex015():
    import random

    # Escreva um programa que pergunte a quantidade de Km percorridos por um
    # carro alugado e a quantidade de dias pelos quais ele foi alugado.
    # Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
    # e R$0,15 por Km rodado.
    print("=== Aluguel de Carro ===")

    # Solicita a quantidade de dias alugados
    print("Quantos dias o carro foi alugado?")

    # Simulando a entrada do usuário com
    # um número aleatório entre 1 e 30
    dias = random.randint(1, 30)  # nosec

    print(f"Você alugou o carro por {dias} dias.\n")

    # Solicita a quantidade de Km percorridos
    print("Quantos Km foram percorridos?")

    # Simulando a entrada do usuário com
    # um número aleatório entre 1 e 1000
    km = random.random() * 1000  # nosec

    print(f"Você percorreu {km:.2f} Km.\n")

    # Calcula o preço total
    preco = (dias * 60) + (km * 0.15)

    # Exibe o resultado
    print(f"O total a pagar é de R${preco:.2f}.\n")

    # Mensagem de encerramento
    print("Obrigado por usar nosso serviço de aluguel de carros!\n")

    # Mensagem de despedida
    print("Até a próxima!\n")

    # Dicas adicionais
    print(
        "Lembre-se: sempre verifique o nível de combustível antes de devolver o carro."
    )
    print("Tenha um ótimo dia e dirija com segurança!")
