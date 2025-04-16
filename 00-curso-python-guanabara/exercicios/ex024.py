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
