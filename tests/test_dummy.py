def test_soma_basica():
    resultado = 1 + 1
    if resultado != 2:
        raise ValueError(f"Erro: esperado 2, mas obteve {resultado}")
