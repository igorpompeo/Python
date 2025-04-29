import os


def test_exercicios_rodam_sem_erros():
    dir_exercicios = os.path.join("Mundo01", "Exercicios")
    arquivos = sorted(
        f
        for f in os.listdir(dir_exercicios)
        if f.startswith("ex") and f.endswith(".py")
    )

    erros = []
    for arquivo in arquivos:
        caminho = os.path.join(dir_exercicios, arquivo)
        print(f"==> Rodando {arquivo}")
        try:
            exec(open(caminho, encoding="utf-8").read())
        except Exception as e:
            erros.append(f"{arquivo}: {e}")
        print("-" * 40)

    assert not erros, "❌ Erros encontrados:\n" + "\n".join(erros)
