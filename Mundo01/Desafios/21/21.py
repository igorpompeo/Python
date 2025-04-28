# Exerc�cio 21
# Faça um programa em python que abra e reproduza um arquivo de áudio no formato mp3.
# Exemplo: Reproduzindo o arquivo de áudio: musica.mp3.
# Importando a biblioteca playsound para reproduzir arquivos de áudio
import pygame
import os

# Descobre a pasta onde o script está
caminho_script = os.path.dirname(os.path.abspath(__file__))

# Lendo o nome do arquivo de áudio do usuário
print('Digite o nome do arquivo de áudio (com extensão .mp3/.wav): ')
# Gerando um nome de arquivo aleatório
arquivo = os.path.join(caminho_script, 'rain.wav')  # Nome do arquivo de áudio
# Exibindo o nome do arquivo
print(f'Você digitou: {arquivo}')
# Verificando se o arquivo existe
if os.path.exists(arquivo):
    pygame.init()  # Inicializando o pygame
    # Reproduzindo o arquivo de áudio
    print(f'Reproduzindo o arquivo de áudio: {arquivo}...')
    # Inicializando o mixer do pygame
    pygame.mixer.music.load(arquivo)
    # Colocando para tocar o arquivo de áudio
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():  # Esperando o áudio terminar de tocar
        continue
else:
    # Exibindo mensagem de erro se o arquivo não existir
    print(f'Erro: O arquivo {arquivo} não foi encontrado.')