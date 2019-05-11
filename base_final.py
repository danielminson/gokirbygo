import pygame
from pygame.locals import *
import sys
import math
from os import path

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Go Kirby Go')

size = [1280, 720]
WHITE = (255, 255, 255)
black = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)



img_dir = path.join(path.dirname(__file__), 'Imagens')


clock = pygame.time.Clock()

CHAO = 0
JUMP = 1

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

def redesenhafundo():
    screen.blit(fundo, (fundoX, 0)) 
    screen.blit(fundo, (fundoX2, 0))  
    screen.blit(cenario, (cenarioX, 0)) 
    screen.blit(cenario, (cenarioX2, 0)) 
    pygame.display.update()


fundo = pygame.image.load(path.join('Imagens','imagem_de_fundo_atual.png')).convert()
fundo.set_colorkey(black)
fundoX = 0
fundoX2 = fundo.get_width()
cenario = pygame.image.load(path.join('Imagens','cenário_atual.png')).convert()
cenario.set_colorkey(black)
cenarioX = 0
cenarioX2 = fundo.get_width()


#Cria o Kirby
player = Player()
# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
speed = 60  

while running:

    for event in pygame.event.get(): 
        player.process_event(event) 
        if event.type == pygame.QUIT: 
            running = False    
            pygame.quit() 
            quit()
    # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.


    all_sprites.update()

    # A cada loop, redesenha o fundo e os sprites
    screen.fill(black)
    redesenhafundo()
    all_sprites.draw(screen)
    
    # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()

    fundoX -= 5
    fundoX2 -= 5
    cenarioX -= 5
    cenarioX2 -= 5
    if fundoX < fundo.get_width() *-1:  
        fundoX = fundo.get_width()
    
    if fundoX2 < fundo.get_width() *-1:
        fundoX2 = fundo.get_width()
        
    if cenarioX < fundo.get_width() *-1:  
        cenarioX = fundo.get_width()
    
    if cenarioX2 < fundo.get_width() *-1:
        cenarioX2 = fundo.get_width()


    clock.tick(speed) 