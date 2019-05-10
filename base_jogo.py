import pygame
import random
from time import sleep 
from os import path

img_dir = path.join(path.dirname(__file__), 'Imagens')

# Dados gerais do jogo.
WIDTH = 1300 # Largura da tela

HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Kirby(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, foto_kirby):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        self.image = foto_kirby
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(foto_kirby, (100, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

        self.speedx = 0
        self.speedy = 0

    #def update(self):
       # self.rect.x += self.speedx
       # self.rect.y += self.speedy
        # Mantem dentro da tela
       # if self.rect.right > WIDTH:
       #     self.rect.right = WIDTH
       # if self.rect.left < 0:
       #     self.rect.left = 0
        self.x = 10
        self.y = 100
        self.speed = 100
        self.isjump=0
        self.massa = 10
        self.force = 6
        F = 0 
    def direita(self):
        self.x+=self.speed 
    def esquerda(self):
        self.x-=self.speed
    def jump(self):
        self.isjump = 1
    def update(self):
        if self.isjump:
            if self.force > 0: 
                F = (0.5*self.massa*(self.force*self.force))
                #mudando de posicao
                self.y = self.y-F
                #velocidade
                self.force = self.force-1
                #chegando no chão
                if self.y == 100:
                    self.y = 100
                    self.isjump = 0
                    self.force = 6
            else:
                F = -0.5*self.massa*(self.force*self.force)
                #mudando de posicao
                self.y = self.y-F
                #velocidade
                self.force = self.force-1
                #chegando no chão
                if self.y == 100:
                    self.y = 100
                    self.isjump = 0
                    self.force = 6

        

def load_assets(img_dir):
	assets = {}
	assets["foto_kirby"] = pygame.image.load(path.join(img_dir, "kirby.png")).convert()
	assets["fundo"] = pygame.image.load(path.join(img_dir, "cenário_atual.png")).convert()
	return assets

#Inicializacao
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Go Kirby Go")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega todos os assets uma vez só e guarda em um dicionário
assets = load_assets(img_dir)

# Carrega o fundo do jogo
background = assets["fundo"]
background_rect = background.get_rect()

kirby = Kirby(assets["foto_kirby"])

all_sprites = pygame.sprite.Group()
all_sprites.add(kirby)

# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    kirby.speedx = -8
                if event.key == pygame.K_RIGHT:
                    kirby.speedx = 8
                if event.key == pygame.K_SPACE:
                	kirby.rect.y += -10
                    
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    kirby.speedx = 0
                if event.key == pygame.K_RIGHT:
                    kirby.speedx = 0
                if event.key == pygame.K_SPACE:
                	kirby.rect.y = HEIGHT

                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()
