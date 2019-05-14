import pygame
from pygame.locals import *
import sys
import math
from os import path

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Go Kirby Go')

fontname = pygame.font.match_font("arial")  #  Fonte da letra usada no score e timer.
font_size = 50

size = [1280, 720]
WHITE = (255, 255, 255)
black = (0, 0, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

img_dir = path.join(path.dirname(__file__), 'Imagens')
png_dir = path.join(path.dirname(__file__), 'Imagens', 'png')

lives=3

clock = pygame.time.Clock()

CHAO = 0
JUMP = 1
score = 0

#Escreve o score na tela
def draw_text(surface, text, font_size, x, y, color):
    font = pygame.font.Font(fontname, font_size)
    text_surface = font.render(text, True, color)
    text_rect=text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


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
<<<<<<< HEAD
        self.image = pygame.transform.scale(player_img, (200, 200))
        
=======
        self.image = pygame.transform.scale(player_img, (100, 100))

>>>>>>> 9877836eb6fcc922a8040109037181840a202e44
        # Deixando transparente.
        self.image.set_colorkey(YELLOW)

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
        self.jumping = False
        self.estado = CHAO

    def process_event(self, event):

        if event.type == pygame.KEYDOWN \
            and event.key == pygame.K_SPACE \
            and self.estado == CHAO:
            self.speedy = -15
            self.estado = JUMP

        if self.estado == CHAO:
            self.speedy = 0
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

class Plataforma(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, x, y, width, height):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Carregando a imagem de fundo
        self.image = pygame.Surface((width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
<<<<<<< HEAD
"""
class Plataforma_Perigosas(pygame.sprite.Sprite):
    # Construindo a classe
    def __init__(self, x,y, width, height):
        #Construtor da classe 
        pygame.sprite.Sprite.__init__(self)
"""
=======

>>>>>>> 9877836eb6fcc922a8040109037181840a202e44
def redesenhafundo():
    screen.blit(mascara, (mascaraX, 0))
    screen.blit(mascara, (mascaraX2, 0))
    screen.blit(fundo, (fundoX, 0))
    screen.blit(fundo, (fundoX2, 0))
    screen.blit(cenario, (cenarioX, 0))
    screen.blit(cenario, (cenarioX2, 0))
    pygame.display.update()


def Menu(screen):
    menu_img = pygame.image.load(path.join(img_dir, "entrada_v1.png")).convert()


#def score(score):  # Funçao que mostra o numero de pontos obtidos pelo jogador.
 #   text = smallfont.render("Pontos:" , black)
  #  screen.blit(text, [0,0])

fundo = pygame.image.load(path.join('Imagens','imagem_de_fundo_atual.png')).convert()
fundo.set_colorkey(black)
fundoX = 0
fundoX2 = fundo.get_width()
cenario = pygame.image.load(path.join('Imagens','cenário_atual.png')).convert()
cenario.set_colorkey(black)
cenarioX = 0
cenarioX2 = cenario.get_width()
mascara = pygame.image.load(path.join('Imagens','mascara_atual.png')).convert()
mascara.set_colorkey(black)
mascaraX=0
mascaraX2=mascara.get_width()

#Cria o Kirby
player = Player()
# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(player)



# Cria as plataformas.
all_platforms = pygame.sprite.Group()

chao = Plataforma(0, HEIGHT - 140, 1280, 150)
all_platforms.add(chao)

running = True
<<<<<<< HEAD
speed = 60
=======
FPS = 30  
>>>>>>> cf502f8cd1fe090c84b5cf62831c38acc8b188f8

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

    # Verifica se houve colisão entre nave e meteoro
    hits = pygame.sprite.spritecollide(player, all_platforms, False, pygame.sprite.collide_rect)
    if hits:
        # Toca o som da colisão
        player.estado = CHAO
        player.speedy = 0


    # A cada loop, redesenha o fundo e os sprites
    screen.fill(WHITE)
    redesenhafundo()
    all_sprites.draw(screen)
    score+=1
    #escreve o score na tela
    draw_text(screen, str(score), font_size, WIDTH/2, 10, BLACK)

    #mostra a vida na tela
    draw_text(screen, chr(9829)*lives, 100, 200, 0, RED)


    # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()

    fundoX -= 5
    fundoX2 -= 5
    cenarioX -= 5
    cenarioX2 -= 5
    mascaraX -=5
    mascaraX2-=5
    if fundoX < fundo.get_width() *-1:
        fundoX = fundo.get_width()

    if fundoX2 < fundo.get_width() *-1:
        fundoX2 = fundo.get_width()

    if cenarioX < cenario.get_width() *-1:
        cenarioX = cenario.get_width()

    if cenarioX2 < cenario.get_width() *-1:
        cenarioX2 = cenario.get_width()

    if mascaraX < mascara.get_width() *-1:
        mascaraX = mascara.get_width()

    if mascaraX2 < mascara.get_width() *-1:
        mascaraX2 = mascara.get_width()


<<<<<<< HEAD
    clock.tick(speed)
=======
    clock.tick(FPS) 
>>>>>>> cf502f8cd1fe090c84b5cf62831c38acc8b188f8
