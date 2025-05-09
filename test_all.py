import importlib.util
import os

import pytest

# Diretórios com os exercícios
diretorios_exercicios = [
    ("Mundo01.Exercicios", os.path.join("Mundo01", "Exercicios")),
    ("Mundo02.Exercicio", os.path.join("Mundo02", "Exercicio")),
]


@pytest.mark.parametrize("mod_base, caminho", diretorios_exercicios)
def test_exercicios_rodam_sem_erros(mod_base, caminho):
    if not os.path.exists(caminho):
        pytest.fail(f"Diretório não encontrado: {caminho}")

    arquivos = sorted(
        f for f in os.listdir(caminho) if f.startswith("ex") and f.endswith(".py")
    )

    for arquivo in arquivos:
        nome_modulo = f"{mod_base}.{arquivo[:-3]}"
        caminho_modulo = os.path.join(caminho, arquivo)

        spec = importlib.util.spec_from_file_location(nome_modulo, caminho_modulo)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)

        func = getattr(modulo, arquivo[:-3], None)
        if callable(func):
            func()  # executa a função exXXX() se existir
        else:
            print(
                f"[AVISO] Função '{arquivo[:-3]}' não encontrada no módulo {nome_modulo}"
            )
