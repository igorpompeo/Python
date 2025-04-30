def ex014():
    import random

    # Título do programa
    print("=== Conversor de Temperatura: Celsius para Fahrenheit ===")

    # Gera um número aleatório entre 0 e 45 para simular a entrada
    celsius = random.random() * 45  # nosec

    # Exibe a temperatura em Celsius
    print(f"\nA temperatura em Celsius é: {celsius:.2f}°C")

    # Mensagem de instrução
    print("\nAgora, vamos fazer a conversão para Fahrenheit.")
    print("Fórmula para conversão: F = C * 9/5 + 32")

    # Realiza o cálculo de conversão
    fahrenheit = celsius * 9 / 5 + 32

    # Exibe o resultado da conversão
    print(f"\nA temperatura em Fahrenheit é: {fahrenheit:.2f}°F")

    # Mensagens de encerramento
    print("\nConversão concluída com sucesso!")
    print("Obrigado por usar o conversor de temperatura!")

    # Mensagens de despedida
    print("\nAté a próxima!")
    print("Se precisar de mais alguma coisa, estarei por aqui!")

    # Dicas adicionais
    print(
        "\nLembre-se: a temperatura em Fahrenheit é "
        "sempre maior que a temperatura em Celsius."
    )
    print("Tenha um ótimo dia e não se esqueça de se manter hidratado!")
