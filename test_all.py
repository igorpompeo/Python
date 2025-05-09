import importlib
import os

import pytest

dir_exercicios = os.path.join("Mundo01", "Exercicios", "Mundo02", "Exercicio")


def test_exercicios_rodam_sem_erros():
    arquivos = sorted(
        f
        for f in os.listdir(dir_exercicios)
        if f.startswith("ex") and f.endswith(".py")
    )
    for arquivo in arquivos:
        modulo = f"Mundo01.Exercicios.Mundo02.Exercicio{arquivo[:-3]}"
        exercicio = importlib.import_module(modulo)

        func = getattr(exercicio, arquivo[:-3], None)
        if callable(func):
            func()  # chama ex001(), ex002(), etc.
        else:
            pytest.fail(f"Função {arquivo[:-3]} não encontrada em {arquivo}")
