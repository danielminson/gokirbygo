# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import random
import time
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'Imagens')

# Dados gerais do jogo.
WIDTH = 1280 # Largura da tela
HEIGHT = 720 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
size = [1280, 720]
WHITE = (255, 255, 255)
black = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
mainState = 0
jumpState = 1
slideState = 2

CHAO = 0
JUMP = 1

def redesenhafundo():
    screen.blit(fundo, (fundoX, 0)) 
    screen.blit(fundo, (fundoX2, 0))  
    pygame.display.update()

# Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo
        player_img = pygame.image.load(path.join(img_dir, "kirby.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (100, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(black)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT -150        
        # Velocidade do kirby
        self.speedx = 0
        self.speedy = 0
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
        self.posX, self.posY = 50, size[1] - 180
        self.rect.center = (self.posX, self.posY)
        self.jumpSpeed = 10
        self.fallSpeed = 11
        self.slideDis = 4
        self.jumping = False
        self.estado = CHAO

    def process_event(self, event):
        print(event.type)

        if event.type == pygame.KEYDOWN \
            and event.key == pygame.K_SPACE \
            and self.estado == CHAO:
            self.speedy = -15
            self.estado = JUMP

        if self.estado == CHAO:
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    self.speedx = -8
                if event.key == pygame.K_RIGHT:
                    self.speedx = 8

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    self.speedx = 0
                if event.key == pygame.K_RIGHT:
                    self.speedx = 0

    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.estado == JUMP:
            self.speedy += 1
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


    def jump(self):
        self.rect.centery -= self.jumpSpeed

    def fall(self):   
        self.rect.centery += self.fallSpeed
    
    def estado_parado(self):
        self.rect.center = self.rect.center
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Kirby")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
timeElapsed = 0
timeReset = 0
# Carrega o fundo do jogo

#background = pygame.image.load(path.join(img_dir, "cenário_atual.png")).convert()
#background_rect = background.get_rect()


fundo = pygame.image.load(path.join('Imagens','cenário_atual.png')).convert()
fundoX = 0
fundoX2 = fundo.get_width()

#Cria o Kirby
player = Player()
# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Comando para evitar travamentos.
try:
    # Loop principal.
    running = True
    while running:

        redesenhafundo() 
        fundoX -= 5
        fundoX2 -= 5

        if fundoX < fundo.get_width() * -1:  
            fundoX = fundo.get_width()
        
        if fundoX2 < fundo.get_width() * -1:
            fundoX2 = fundo.get_width()

        clockTime = clock.tick(60)
        timeElapsed += clockTime
        timeSec = timeElapsed / 1000
        timeElapsed += clockTime

        for event in pygame.event.get():
            player.process_event(event)

            if event.type == pygame.QUIT:
                running = False

        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(black)
        #screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    
    pygame.quit()
