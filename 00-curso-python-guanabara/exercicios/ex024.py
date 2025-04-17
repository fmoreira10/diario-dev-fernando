# 🎵 Como tocar um arquivo de áudio (MP3) usando Pygame?
#
# Este programa utiliza a biblioteca Pygame para carregar e reproduzir
# um arquivo de música em formato MP3. A função `pygame.mixer.music.load()`
# carrega o áudio, e `pygame.mixer.music.play()` inicia a reprodução.
# O `try/except` é usado para capturar erros no carregamento.
# O loop `while` mantém o programa em execução enquanto a música está tocando.

import pygame

pygame.init()
pygame.mixer.init()

try:
    pygame.mixer.music.load("ex024.mp3")
    print("Arquivo carregado com sucesso!")
    pygame.mixer.music.play()
    print("Música tocando...")
except pygame.error as e:
    print(f"Erro ao carregar o arquivo de áudio: {e}")

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
