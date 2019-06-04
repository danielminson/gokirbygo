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

#atributos da tela
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Go Kirby Go')

#Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# ------------------- DIRETORIOS DE IMAGENS -------------------------------
img_dir = path.join(path.dirname(__file__), 'Imagens')
cenarios_dir = path.join(path.dirname(__file__), 'Imagens', 'Imagens_Fundo')
obs_dir = path.join(path.dirname(__file__), 'Imagens', 'Obstaculos')
snr_dir = path.join(path.dirname(__file__))
snd_dir = path.join(path.dirname(__file__), "Som")
fnt_dir = path.join(path.dirname(__file__), 'Fontes')
kirby_dir = path.join(path.dirname(__file__), 'Imagens', 'Kirby') #kirby andando
kv_dir = path.join(path.dirname(__file__),"Imagens","Kirby_voando") # kirby voando
kb_dir = path.join(path.dirname(__file__),"Imagens","KirbySword")#Kirby para batalha
PikaChu = path.join(path.dirname(__file__),"Imagens","PikachuMonstro")#Imagem do Monstro
# -------------------------------------------------------------------------

#Estados --------------------------------
CHAO = 0
PULANDO = 1
ANDANDO = 2
# ----------------------------------------

#FPS do jogo
FPS = 30

#------------------- CLASSES -------------------------

# Classe Jogador (Kirby)
class Player(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self,kirby_andando,kirby_voando):
        # Construtor da classe pai (Sprite).



        # -------------------------------------------- Imagens do Kirby andando --------------------------------------------
        pygame.sprite.Sprite.__init__(self)

        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 0.2

        self.andando = kirby_andando
        self.pulando = kirby_voando

        self.index = 0
        self.image = self.andando[self.index]
        self.rect = self.image.get_rect()

        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT -140
        # Velocidade do kirby
        self.speedx = 0
        self.speedy = 0

        self.estado = ANDANDO

    def process_event(self, event):

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.speedy==0:
            self.speedy = -20
            self.estado = PULANDO

        if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = -10
                if event.key == pygame.K_RIGHT:
                    player.speedx = 10

    def update(self):

        #when the update method is called, we will increment the index
        self.index += 1
        if self.estado == ANDANDO:
            if self.index >= len(self.andando):
                self.index = 0
            self.image = self.andando[self.index]

        if self.estado == PULANDO:
            if self.index >= len(self.pulando):
                self.index = 0
            self.image = self.pulando[self.index]

        self.rect.x += self.speedx
        self.rect.y += self.speedy
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


#Classe que cria as plataformas voadoras
class Plataforma_voadora(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):

        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10

        self.image = pygame.image.load(path.join(cenarios_dir, "plataforma_voadora.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = int(self.rect.width * .85 / 2)


    def update(self):
        self.rect.x -= self.vel
        if self.rect.x < -self.width:
            self.kill()

#Classe obstaculos
class Obstaculo(pygame.sprite.Sprite):
    # Construindo a classe
    def __init__(self, x, y, width, height):

        #Construtor da classe
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10

        self.image = imagem_aleatoria()

        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLUE)
        self.rect.x = x
        self.rect.y = y
        self.radius = int(self.rect.width * .85 / 2)

    def update(self):
        self.rect.x -= self.vel
        if self.rect.x < -self.width:
            self.kill()
        if hits_obstaculos:
            self.kill()
# --------------------- FUNÇÕES ------------------------

#Funcao que carrega as imagens de obstaculos
def imagem_aleatoria():
    obs_img1 = pygame.image.load(path.join(obs_dir, "arbusto_tipo2.png")).convert()

    obs_img2 = pygame.image.load(path.join(obs_dir, "casinha.png")).convert()

    obs_img3 = pygame.image.load(path.join(obs_dir, "pedra.png")).convert()

    obs_img4 = pygame.image.load(path.join(obs_dir, "arbusto_tipo1.png")).convert()

    obs_img5 = pygame.image.load(path.join(obs_dir, "arvore.png")).convert()

    obs_img6 = pygame.image.load(path.join(obs_dir, "obstaculo1.png")).convert()

    rotate = [obs_img1,obs_img2,obs_img3,obs_img4,obs_img5,obs_img6]

    return pygame.transform.scale(rotate[random.randint(0, 5)], (260,200))

#Funcao que atualiza os fundos e desenha na tela
def redesenhafundo(fundo,fundoX,fundoX2,chao,chaoX,chaoX2):
    screen.blit(fundo, (fundoX, 0))
    screen.blit(fundo, (fundoX2, 0))
    screen.blit(chao, (chaoX, 0))
    screen.blit(chao, (chaoX2, 0))
    pygame.display.update()

def Menu():
    #Converte a imagem de menu
    load_data()
    menu_img = pygame.image.load(path.join(cenarios_dir, "menu_entrada.png")).convert()
    menu_rect = menu_img.get_rect()
    help_img = pygame.image.load(path.join(cenarios_dir, "menu_help.png")).convert()
    help_rect = help_img.get_rect()

    intro = True
    tela_help = False
    back = False
    highscore = load_data()

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    intro = False
                if event.key == pygame.K_h:
                    tela_help = True
                if event.key == pygame.K_b:
                    back = True
                    tela_help = False
        if tela_help == False:
            screen.fill(BLACK)
            screen.blit(menu_img,menu_rect)
            draw_text(screen, fontname , "Highscore: "+str(highscore), WIDTH/2, 10, WHITE)
            pygame.display.flip()
            clock.tick(15)

        if tela_help == True:
            screen.fill(BLACK)
            screen.blit(help_img,help_rect)
            draw_text(screen, fontname, "Highscore: "+str(highscore), WIDTH/2, 10, WHITE)
            pygame.display.flip()
            clock.tick(15)

        if back == False and tela_help == True:
            screen.fill(BLACK)
            screen.blit(help_img,help_rect)
            draw_text(screen, fontname, "Highscore: "+str(highscore), WIDTH/2, 10, WHITE)
            pygame.display.flip()
            clock.tick(15)

        if back == True and tela_help == False:
            screen.fill(BLACK)
            screen.blit(menu_img,menu_rect)
            draw_text(screen, fontname, "Highscore: "+str(highscore), WIDTH/2, 10, WHITE)
            pygame.display.flip()
            clock.tick(15)

def load_assets(img_dir,cenarios_dir,obs_dir,snd_dir,fnt_dir,kirby_dir,kv_dir):
    assets = {}
    assets["fundo_grama"] = pygame.image.load(path.join(cenarios_dir,'imagem_de_fundo.png')).convert()
    assets["fundo_castelo"] = pygame.image.load(path.join(cenarios_dir,'imagem_de_fundo2.png')).convert()
    assets["fundo_espaco"] = pygame.image.load(path.join(cenarios_dir,'imagem_de_fundo3.png')).convert()
    assets["chao_grama"] = pygame.image.load(path.join(cenarios_dir,'chao.png')).convert()
    assets["chao_nuvem"] = pygame.image.load(path.join(cenarios_dir,'chao2.png')).convert()
    assets["chao_arcoiris"] = pygame.image.load(path.join(cenarios_dir,'chao3.png')).convert()
    assets["som_colisao"] = pygame.mixer.Sound(path.join(snd_dir, 'hit_sound.ogg'))
    assets["som_vida"] = pygame.mixer.Sound(path.join(snd_dir, 'hit_sound2.ogg'))
    assets["musica_fundo"] = pygame.mixer.Sound(path.join(snd_dir, 'kirby_star_ride.ogg'))
    assets["fonte_score"] = pygame.font.Font(path.join(fnt_dir, "Retron2000.ttf"),50)
    assets["fonte_coracao"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"),50)
    X1 = 0
    kirby_andando = []

    while X1 < 8:
        F_name = 'k0{0}.png'.format(X1)
        imagem_andando = pygame.image.load(path.join(kirby_dir,F_name)).convert()
        imagem_andando =  pygame.transform.scale(imagem_andando,(200,200))
        imagem_andando.set_colorkey(WHITE)
        kirby_andando.append(imagem_andando)
        X1 += 1
    assets["kirby_andando"] = kirby_andando


    X2 = 0
    kirby_voando = []
    while X2 < 26:
        F_name = 'Kirbyvoando-0{0}.png'.format(X2)
        imagem_pulando = pygame.image.load(path.join(kv_dir,F_name)).convert()
        imagem_pulando =  pygame.transform.scale(imagem_pulando,(200,200))
        imagem_pulando.set_colorkey(WHITE)
        kirby_voando.append(imagem_pulando)
        X2 += 1
    assets["kirby_voando"] = kirby_voando

    return assets

#----------------- SONS/IMAGENS/FONTES ------------------------------
assets = load_assets(img_dir,cenarios_dir,obs_dir,snd_dir,fnt_dir,kirby_dir,kv_dir)
#Carrega as Imagens de Fundo e da plataforma de chao

#Cenário 1 -----------------------------------------------------------------------------
fundo_score1 = assets["fundo_grama"]
fundoX_score1 = 0
fundoX2_score1 = fundo_score1.get_width()

chao_grama = assets["chao_grama"]
chao_grama.set_colorkey(BLACK)
chao_gramaX = 0
chao_gramaX2 = chao_grama.get_width()

#Cenário 2 ------------------------------------------------------------------------------
fundo_score2 = assets["fundo_castelo"]
fundoX_score2 = 0
fundoX2_score2 = fundo_score2.get_width()

chao_nuvem = assets["chao_nuvem"]
chao_nuvem.set_colorkey(GREEN)
chao_nuvemX = 0
chao_nuvemX2 = chao_nuvem.get_width()

#Cenário 3 ------------------------------------------------------------------------------
fundo_score3 = assets["fundo_espaco"]
fundoX_score3 = 0
fundoX2_score3 = fundo_score3.get_width()

chao_arcoiris = assets["chao_arcoiris"]
chao_arcoiris.set_colorkey(BLACK)
chao_arcoirisX = 0
chao_arcoirisX2 = chao_arcoiris.get_width()

#--------------- CRIAÇÃO DOS ELEMENTOS DO JOGO -------------------
#Cria o Kirby
player = Player(assets["kirby_andando"],assets["kirby_voando"])

# Cria um grupo de todos os sprites e adiciona o Kirby
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#Cria os obstaculos
obstacles = pygame.sprite.Group()
pygame.time.set_timer(USEREVENT+2, random.randrange(1000,5000)) #a cada 1 ate 8 segundos ira aparecer obstaculos
