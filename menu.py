# menu.py
import importlib
import os

# Caminho para o arquivo do módulo
caminho = "Mundo01/Exercicios/ex001.py"

# Verifica se o arquivo existe
if os.path.exists(caminho):
    # Em vez de usar exec(), use importlib para carregar o módulo
    nome_modulo = caminho.replace(".py", "").replace("/", ".")
    modulo = importlib.import_module(nome_modulo)
    # Agora você pode usar as funções ou variáveis do módulo importado
else:
    print(f"Arquivo {caminho} não encontrado.")
