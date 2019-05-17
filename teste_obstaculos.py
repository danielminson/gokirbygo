import pygame
from pygame.locals import *
import sys
import math
from os import path
import random

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
bos_dir = path.join(path.dirname(__file__), 'Imagens', 'boss')
cen_dir = path.join(path.dirname(__file__), 'Imagens', 'cenario')
plat_dir = path.join(path.dirname(__file__), 'Imagens', 'plataforma')
obs_dir = path.join(path.dirname(__file__), 'Imagens', 'obstaculo')

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
        self.image = pygame.transform.scale(player_img, (200, 200))

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

class Plataforma_Perigosas(pygame.sprite.Sprite):
    # Construindo a classe
    def __init__(self):
        #Construtor da classe
        #Posição minima de x  e uma posição fixa para o y
        self.posX = 100
        self.posY = HEIGHT - 150
        #Posição maxima de x
        self.maxPosX = self.posX * 2

        pygame.sprite.Sprite.__init__(self)
        obs_img1 = pygame.image.load(path.join(obs_dir, "arbusto_tipo2.png")).convert()
        obs_img1.set_colorkey(BLUE)
        self.image1 = obs_img1

        #obs_img1.fill(self.RED)

        obs_img2 = pygame.image.load(path.join(obs_dir, "casinha.png")).convert()
        obs_img2.set_colorkey(BLUE)
        self.image2 = obs_img2
        #obs_img2.fill(self.RED)

        obs_img3 = pygame.image.load(path.join(obs_dir, "pedra.png")).convert()
        obs_img3.set_colorkey(BLUE)
        self.image3 = obs_img3

        #obs_img3.fill(self.RED)

        obs_img4 = pygame.image.load(path.join(obs_dir, "arbusto_tipo1.png")).convert()
        obs_img4.set_colorkey(BLUE)
        self.image4 = obs_img4

        #obs_img4.fill(self.RED)

        obs_img5 = pygame.image.load(path.join(obs_dir, "arvore.png")).convert()
        obs_img5.set_colorkey(BLUE)
        self.image5 = obs_img5
        #obs_img5.fill(self.RED)

        obs_img6 = pygame.image.load(path.join(obs_dir, "obstaculo1.png")).convert()
        obs_img6.set_colorkey(BLUE)
        self.image6 = obs_img6
        #obs_img6.fill(self.RED)

    def update(self):
        self.rect.centerx -= self.speedx

    def reset(self):
        obstaculo = random.randint(0,1)
        #Ira ter uma probabiliade de 1/2 para ter obstaculo == Plataforma_perigosa
        if obstaculo == 0:
            self.rect.center = (random.randrange(self.posX,self.maxPosX),self.posY)
        else:
            self.rect.center = (random.randrange(self.posX,self.maxPosX),self.posY)

def redesenhafundo():
    screen.blit(fundo, (fundoX, 0))
    screen.blit(fundo, (fundoX2, 0))
    screen.blit(cenario, (cenarioX, 0))
    screen.blit(cenario, (cenarioX2, 0))
    pygame.display.update()


def Menu(screen):
    menu_img = pygame.image.load(path.join(cen_dir, "entrada_v1.png")).convert()


#def score(score):  # Funçao que mostra o numero de pontos obtidos pelo jogador.
 #   text = smallfont.render("Pontos:" , black)
  #  screen.blit(text, [0,0])
  
#Cria as plataformas perigosas em cima do chao
all_platforms_per = pygame.sprite.Group()
obstaculo = Plataforma_Perigosas()
all_platforms_per.add()
fundo = pygame.image.load(path.join('Imagens','imagem_de_fundo_atual.png')).convert()
fundo.set_colorkey(black)
fundoX = 0
fundoX2 = fundo.get_width()
cenario = pygame.image.load(path.join('Imagens','cenario','cenário_atual.png')).convert()
cenario.set_colorkey(black)
cenarioX = 0
cenarioX2 = cenario.get_width()

#Cria o Kirby
player = Player()

# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Cria as plataformas.
all_platforms = pygame.sprite.Group()
chao = Plataforma(0, HEIGHT - 140, 1280, 150)
all_platforms.add(chao)



running = True
FPS = 30

#Loop Principal
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

    hits_2 = pygame.sprite.spritecollide(player, all_platforms_per, False, pygame.sprite.collide_circle)
    if hits_2:
        running = False

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

    if fundoX < fundo.get_width() *-1:
        fundoX = fundo.get_width()

    if fundoX2 < fundo.get_width() *-1:
        fundoX2 = fundo.get_width()

    if cenarioX < cenario.get_width() *-1:
        cenarioX = cenario.get_width()

    if cenarioX2 < cenario.get_width() *-1:
        cenarioX2 = cenario.get_width()

    clock.tick(FPS)
