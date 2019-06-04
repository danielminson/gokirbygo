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