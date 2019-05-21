import pygame
from pygame.locals import *
import sys
import math
from os import path
import random
import time


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Go Kirby Go')

fontname = pygame.font.match_font("arial")  # Fonte da letra usada no score e timer.
font_size = 50

size = [1280, 720]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Diretorios de imagens
img_dir = path.join(path.dirname(__file__), 'Imagens')
cenarios_dir = path.join(path.dirname(__file__), 'Imagens', 'cenario')
obs_dir = path.join(path.dirname(__file__), 'Imagens', 'obstaculo')
snr_dir = path.join(path.dirname(__file__))

lives=3
clock = pygame.time.Clock()

CHAO = 0
JUMP = 1
score = 0

colisaojaaconteceu = False
#Escreve o score na tela
def draw_text(surface, text, font_size, x, y, color):
    font = pygame.font.Font(fontname, font_size)
    text_surface = font.render(text, True, color)
    text_rect=text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# Classe Jogador (Kirby)
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
        self.rect.bottom = HEIGHT -140
        # Velocidade do kirby
        self.speedx = 0
        self.speedy = 0
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 7.5
        self.estado = CHAO
        self.vida = 3

    def process_event(self, event):

        if event.type == pygame.KEYDOWN \
            and event.key == pygame.K_SPACE \
            and self.estado == CHAO:
            self.speedy = -17
            self.estado = JUMP

        if self.estado == CHAO:
            self.speedy = 0

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

#Funcao que cria a plataforma principal
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

def imagem_aleatoria():
    obs_img1 = pygame.image.load(path.join(obs_dir, "arbusto_tipo2.png")).convert()
    obs_img1.set_colorkey(BLUE)

    obs_img2 = pygame.image.load(path.join(obs_dir, "casinha.png")).convert()
    obs_img2.set_colorkey(BLUE)

    obs_img3 = pygame.image.load(path.join(obs_dir, "pedra.png")).convert()
    obs_img3.set_colorkey(BLUE)

    obs_img4 = pygame.image.load(path.join(obs_dir, "arbusto_tipo1.png")).convert()
    obs_img4.set_colorkey(BLUE)

    obs_img5 = pygame.image.load(path.join(obs_dir, "arvore.png")).convert()
    obs_img5.set_colorkey(BLUE)

    obs_img6 = pygame.image.load(path.join(obs_dir, "obstaculo1.png")).convert()
    obs_img6.set_colorkey(BLUE)

    rotate = [obs_img1,obs_img2,obs_img3,obs_img4,obs_img5,obs_img6]

    return pygame.transform.scale(rotate[random.randint(0, 5)], (200,200))

class Obstaculo(pygame.sprite.Sprite):
    # Construindo a classe
    def __init__(self, x, y, width, height):

        #Construtor da classe
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8

        self.image = imagem_aleatoria()

        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLUE)
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.x -= self.vel
        if self.rect.x < -self.width:
            self.kill()

#Funcao que atualiza os fundos e desenha na tela
def redesenhafundo():
    screen.blit(fundo, (fundoX, 0))
    screen.blit(fundo, (fundoX2, 0))
    screen.blit(cenario_plataforma, (cenario_plataformaX, 0))
    screen.blit(cenario_plataforma, (cenario_plataformaX2, 0))
    pygame.display.update()

def Menu():
    #Converte a imagem de menu
    menu_img = pygame.image.load(path.join(cenarios_dir, "entrada_v2.png")).convert()
    menu_rect = menu_img.get_rect()
    help_img = pygame.image.load(path.join(cenarios_dir, "help_v1.png")).convert()
    help_rect = help_img.get_rect()

    intro = True
    pause = False
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    intro = False
                if event.key == pygame.K_h:
                    screen.blit(help_img,help_rect)

        screen.fill(BLACK)
        screen.blit(menu_img,menu_rect)
        pygame.display.flip()
        clock.tick(15)
def gameover():
    gameover_img = pygame.image.load(path.join(cenarios_dir, "game_over.png")).convert()
    gameover_rect = gameover_img.get_rect()
    screen.fill(BLACK)
    screen.blit(gameover_img,gameover_rect)
    pygame.display.flip()
    clock.tick(15)
# Carrega os sons do jogo
pygame.mixer.music.load(path.join(snr_dir, 'kirby_star_ride.ogg'))
pygame.mixer.music.set_volume(0.4)


fundo = pygame.image.load(path.join(cenarios_dir,'imagem_de_fundo.png')).convert()
fundo.set_colorkey(BLACK)
fundoX = 0
fundoX2 = fundo.get_width()
cenario_plataforma = pygame.image.load(path.join(cenarios_dir,'cenário_atual.png')).convert()
cenario_plataforma.set_colorkey(BLACK)
cenario_plataformaX = 0
cenario_plataformaX2 = cenario_plataforma.get_width()

#Cria o Kirby
player = Player()
# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Cria as plataformas.
all_platforms = pygame.sprite.Group()

#Plataforma principal de chao
chao = Plataforma(0, HEIGHT - 150, 1280, 140)
all_platforms.add(chao)

running = True
FPS = 30

obstacles = pygame.sprite.Group()

#a cada x tempo ira aparecer obstaculos
pygame.time.set_timer(USEREVENT+2, 8000)
Menu()
while running:
    for event in pygame.event.get():
        player.process_event(event)
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                running = False
                pause = True
                if pause == True:
                    while pause == True:
                        game_paused_img = pygame.image.load(path.join(cenarios_dir, "game_paused.png")).convert()
                        game_paused_rect = game_paused_img.get_rect()
                        screen.fill(BLACK)
                        screen.blit(game_paused_img,game_paused_rect)
                        pygame.display.flip()
                        clock.tick(15)
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                pause = False
            running = True
        if event.type == USEREVENT+2:
            r = random.randrange(0,2)
            if r == 0 or r ==1:
                new_obstacle = Obstaculo(810, HEIGHT-300, 20, 20)
                obstacles.add(new_obstacle)
                all_sprites.add(new_obstacle)

    # Depois de processar os eventos.
    # Atualiza a acao de cada sprite.
    all_sprites.update()

    # Verifica se houve colisão entre nave e meteoro
    hits = pygame.sprite.spritecollide(player, all_platforms, False, pygame.sprite.collide_rect)
    if hits:
        # Toca o som da colisão
        player.estado = CHAO
        player.speedy = 0

    hits2 = pygame.sprite.spritecollide(player,obstacles , False, pygame.sprite.collide_circle)
    if hits2:
        print("morreu")
        running = False

    # A cada loop, redesenha o fundo e os sprites
    screen.fill(WHITE)
    redesenhafundo()
    all_sprites.draw(screen)

    score+=1
    #escreve o score na tela
    draw_text(screen, str(score), font_size, WIDTH/2, 10, BLACK)

    #mostra a vida na tela
    draw_text(screen, chr(9829)*lives, 100, 200, 0, (255,0,0,10))

    # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()

    #Velocidade dos fundos
    fundoX -= 8
    fundoX2 -= 8
    cenario_plataformaX -= 10
    cenario_plataformaX2 -= 10

    if fundoX < fundo.get_width() *-1:
        fundoX = fundo.get_width()

    if fundoX2 < fundo.get_width() *-1:
        fundoX2 = fundo.get_width()

    if cenario_plataformaX < cenario_plataforma.get_width() *-1:
        cenario_plataformaX = cenario_plataforma.get_width()

    if cenario_plataformaX2 < cenario_plataforma.get_width() *-1:
        cenario_plataformaX2 = cenario_plataforma.get_width()

# This should go in the game loop

    clock.tick(FPS)
gameover()
time.sleep(5)
