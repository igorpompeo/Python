# Exerc�cio 21
# Faça um programa em python que abra e reproduza um arquivo de áudio no formato mp3.
# Exemplo: Reproduzindo o arquivo de áudio: musica.mp3.
# Importando a biblioteca playsound para reproduzir arquivos de áudio
import pygame
import os
# Lendo o nome do arquivo de áudio do usuário
print('Digite o nome do arquivo de áudio (com extensão .mp3/.wav): ')
# Gerando um nome de arquivo aleatório
arquivo = os.path.join('C:\\Windows\\Media', 'Windows Shutdown.wav')  # Nome do arquivo de áudio
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
    pygame.event.wait()  # Esperando o áudio terminar de tocar
else:
    # Exibindo mensagem de erro se o arquivo não existir
    print(f'Erro: O arquivo {arquivo} não foi encontrado.')
# Exibindo mensagem de erro se o arquivo não existir
print(f'Erro: O arquivo {arquivo} não foi encontrado.')
