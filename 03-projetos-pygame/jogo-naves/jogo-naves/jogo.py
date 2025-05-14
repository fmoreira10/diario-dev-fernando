import pygame
import sys
import random
from datetime import datetime, timedelta

# Inicialize o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo de Nave Espacial")

# Carregando imagens
nave_img = pygame.image.load("nave.png")
asteroide_img = pygame.image.load("asteroide.png")
background_img = pygame.image.load("espaco.jpg")

# Configurações de pontuação
PONTOS_POR_TEMPO = 10
PONTOS_ASTEROIDE = {30: 5, 50: 10, 70: 20}

# Classe da Nave
class NaveEspacial:
    def __init__(self):
        self.image = nave_img
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - 50))
        self.velocidade = 5
        self.campo_forca_ativo = False
        self.tempo_campo_forca = datetime.now() - timedelta(seconds=30)
        self.tempo_duracao_campo_forca = timedelta(seconds=10)
        self.pontuacao = 0
        self.tiros = []
        self.tiros_traseiros = []
        self.tempo_tiro = datetime.now()

    def mover(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.velocidade
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += self.velocidade

    def ativar_campo_forca(self):
        tempo_decorrido = datetime.now() - self.tempo_campo_forca
        if tempo_decorrido >= timedelta(seconds=30):
            self.campo_forca_ativo = True
            self.tempo_campo_forca = datetime.now()

    def atualizar_campo_forca(self):
        if self.campo_forca_ativo and datetime.now() - self.tempo_campo_forca >= self.tempo_duracao_campo_forca:
            self.campo_forca_ativo = False

    def disparar_bolha(self):
        if (datetime.now() - self.tempo_tiro).seconds >= 1:
            self.tiros.append(pygame.Rect(self.rect.centerx, self.rect.top, 10, 10))
            self.tempo_tiro = datetime.now()

    def disparar_traseiros(self):
        if (datetime.now() - self.tempo_tiro).seconds >= 1:
            self.tiros_traseiros.append(pygame.Rect(self.rect.centerx, self.rect.bottom, 10, 10))
            self.tempo_tiro = datetime.now()

    def atualizar_tiros(self):
        for tiro in self.tiros[:]:
            tiro.y -= 5
            if tiro.bottom < 0:
                self.tiros.remove(tiro)

        for tiro_traseiro in self.tiros_traseiros[:]:
            tiro_traseiro.y += 5
            if tiro_traseiro.top > screen_height:
                self.tiros_traseiros.remove(tiro_traseiro)

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)
        if self.campo_forca_ativo:
            pygame.draw.circle(tela, (0, 255, 255), self.rect.center, 50, 2)

        for tiro in self.tiros:
            pygame.draw.circle(tela, (0, 255, 0), tiro.center, 5)

        for tiro_traseiro in self.tiros_traseiros:
            pygame.draw.circle(tela, (255, 0, 0), tiro_traseiro.center, 5)

# Classe do Asteroide
class Asteroide:
    def __init__(self, x, y, tamanho):
        self.tamanho = tamanho
        self.image = pygame.transform.scale(asteroide_img, (tamanho, tamanho))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocidade = random.randint(2, 4)

    def mover(self):
        self.rect.y += self.velocidade

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)

# Função para mostrar a pontuação
def exibir_pontuacao(tela, pontuacao, tempo_inicio):
    tempo_jogo = (datetime.now() - tempo_inicio).seconds
    pontos_tempo = tempo_jogo * PONTOS_POR_TEMPO
    pontuacao_total = pontuacao + pontos_tempo

    fonte = pygame.font.SysFont(None, 36)
    texto = fonte.render(f"Pontuação: {pontuacao_total}", True, (255, 255, 255))
    tela.blit(texto, (10, 10))
    return pontuacao_total

# Tela de fim de jogo
def game_over_screen(tela, pontuacao):
    fonte = pygame.font.SysFont(None, 48)
    texto = fonte.render(f"Fim de Jogo! Pontuação Final: {pontuacao}", True, (255, 0, 0))
    tela.blit(texto, (screen_width // 2 - texto.get_width() // 2, screen_height // 2))
    pygame.display.flip()
    pygame.time.delay(3000)

# Função principal do jogo
def jogo():
    nave = NaveEspacial()
    asteroides = [Asteroide(random.randint(0, screen_width - 50), -50, random.choice([30, 50, 70]))]
    clock = pygame.time.Clock()
    tempo_inicio = datetime.now()
    running = True

    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    nave.ativar_campo_forca()
                if event.key == pygame.K_i:
                    nave.disparar_bolha()
                if event.key == pygame.K_o:
                    nave.disparar_traseiros()

        nave.mover(keys)
        nave.atualizar_campo_forca()
        nave.atualizar_tiros()

        for asteroide in asteroides[:]:
            asteroide.mover()
            if asteroide.rect.colliderect(nave.rect):
                if nave.campo_forca_ativo:
                    continue  # Ignore a colisão
                else:
                    game_over_screen(screen, nave.pontuacao)
                    running = False
            elif asteroide.rect.top > screen_height:
                nave.pontuacao += PONTOS_ASTEROIDE[asteroide.tamanho]
                asteroides.remove(asteroide)

        if random.random() < 0.02:
            tamanho = random.choice([30, 50, 70])
            x_novo = random.randint(0, screen_width - tamanho)
            asteroides.append(Asteroide(x_novo, -tamanho, tamanho))

        screen.blit(background_img, (0, 0))
        nave.desenhar(screen)
        for asteroide in asteroides:
            asteroide.desenhar(screen)

        exibir_pontuacao(screen, nave.pontuacao, tempo_inicio)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Iniciar o jogo
jogo()

