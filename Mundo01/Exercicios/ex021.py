import pygame
import os

# Detecta se está rodando no GitHub Actions
modo_github = os.getenv('GITHUB_ACTIONS') == 'true'

# Descobre a pasta onde o script está
caminho_script = os.path.dirname(os.path.abspath(__file__))

# Pergunta o nome do arquivo de áudio
nome_audio = 'rain.wav' if modo_github else input('Digite o nome do arquivo de áudio (com extensão .mp3/.wav): ').strip()

# Tenta montar o caminho relativo à pasta do script
caminho_arquivo = os.path.join(caminho_script, nome_audio)

# Se não encontrar lá, tenta na pasta de execução atual
if not os.path.exists(caminho_arquivo):
    caminho_arquivo = nome_audio

print(f'Procurando o arquivo: {caminho_arquivo}')

if os.path.exists(caminho_arquivo):
    if modo_github:
        print(f'(Simulando reprodução de áudio: {caminho_arquivo})')
    else:
        pygame.init()
        pygame.mixer.init()
        print(f'Reproduzindo o arquivo de áudio: {caminho_arquivo}...')
        pygame.mixer.music.load(caminho_arquivo)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            continue
else:
    print(f'Erro: O arquivo {caminho_arquivo} não foi encontrado.')
