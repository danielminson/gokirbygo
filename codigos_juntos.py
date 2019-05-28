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

#------------------- DIRETORIOS DE IMAGENS -------------------------------
img_dir = path.join(path.dirname(__file__), 'Imagens')
cenarios_dir = path.join(path.dirname(__file__), 'Imagens', 'cenario')
obs_dir = path.join(path.dirname(__file__), 'Imagens', 'obstaculo')
snr_dir = path.join(path.dirname(__file__))
snd_dir = path.join(path.dirname(__file__), "Som")
fnt_dir = path.join(path.dirname(__file__), 'font')
kirby_dir = path.join(path.dirname(__file__), 'Imagens', 'Kirby') #kirby andando
#-------------------------------------------------------------------------

#Estados
CHAO = 0
JUMP = 1

#FPS do jogo
FPS = 30

#------------------- CLASSES -------------------------

# Classe Jogador (Kirby)
class Player(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self):
        # Construtor da classe pai (Sprite).

        pygame.sprite.Sprite.__init__(self)
# -------------------------------------------- Imagens do Kirby andando --------------------------------------------

        k0 = pygame.image.load(path.join(kirby_dir, "0.png")).convert()
        k0.set_colorkey(WHITE)
        k0 = pygame.transform.scale(k0,(200,200))

        k1 = pygame.image.load(path.join(kirby_dir, "1.png")).convert()
        k1.set_colorkey(WHITE)
        k1 = pygame.transform.scale(k1,(200,200))


        k2 = pygame.image.load(path.join(kirby_dir, "2.png")).convert()
        k2.set_colorkey(WHITE)
        k2 = pygame.transform.scale(k2,(200,200))


        k3 = pygame.image.load(path.join(kirby_dir, "3.png")).convert()
        k3.set_colorkey(WHITE)
        k3 = pygame.transform.scale(k3,(200,200))


        k4 = pygame.image.load(path.join(kirby_dir, "4.png")).convert()
        k4.set_colorkey(WHITE)
        k4 = pygame.transform.scale(k4,(200,200))


        k5 = pygame.image.load(path.join(kirby_dir, "5.png")).convert()
        k5.set_colorkey(WHITE)
        k5 = pygame.transform.scale(k5,(200,200))


        k6 = pygame.image.load(path.join(kirby_dir, "6.png")).convert()
        k6.set_colorkey(WHITE)
        k6 = pygame.transform.scale(k6,(200,200))


        k7 = pygame.image.load(path.join(kirby_dir, "7.png")).convert()
        k7.set_colorkey(WHITE)
        k7 = pygame.transform.scale(k7,(200,200))

#------------------------------------- acabou as imagens ---------------------------------------

        self.images = [k0,k1,k2,k3,k4,k5,k6,k7]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT -140
        # Velocidade do kirby
        self.speedx = 0
        self.speedy = 0

        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 0.2

    def process_event(self, event):

        if event.type == pygame.KEYDOWN \
            and event.key == pygame.K_SPACE \
            and self.speedy == 0:
            self.speedy = -16

    def update(self):
        self.index += 1
        if self.index >= 8:
            self.index = 0

        self.image = self.images[self.index]

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        self.speedy += 1

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.top < 0:
            self.rect.top = 0

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

#Classe dos cogumelos
class Cogumelo(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):

        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10

        imagex = pygame.image.load(path.join(obs_dir, "mushroom 1up.png")).convert()
        self.image = pygame.transform.scale(imagex,(126,100))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLUE)
        self.rect.x = x
        self.rect.y = y
        self.radius = int(self.rect.width * 1.2)
    def update(self):
        self.rect.x -= self.vel
        if self.rect.x < -self.width:
            self.kill()
        if hits_cogumelo:
            self.kill()

#Classe que cria as plataformas voadoras
class Plataforma_voadora(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):

        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10

        self.image = pygame.image.load(path.join(cenarios_dir, "plataforma_tipo2.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = int(self.rect.width * .85 / 2)


    def update(self):
        self.rect.x -= self.vel
        if self.rect.x < -self.width:
            self.kill()

#--------------------- FUNÇÕES ------------------------

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
def redesenhafundo():
    screen.blit(fundo, (fundoX, 0))
    screen.blit(fundo, (fundoX2, 0))
    screen.blit(cenario_plataforma, (cenario_plataformaX, 0))
    screen.blit(cenario_plataforma, (cenario_plataformaX2, 0))
    pygame.display.update()

#Escreve o score na tela
def draw_text(surface, fontname, text, x, y, color):
    font = fontname
    text_surface = font.render(text, True, color)
    text_rect=text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

#Funcao que cria o Menu
def Menu():
    #Converte a imagem de menu
    load_data()
    menu_img = pygame.image.load(path.join(cenarios_dir, "entrada_v2.png")).convert()
    menu_rect = menu_img.get_rect()
    help_img = pygame.image.load(path.join(cenarios_dir, "help_v1.png")).convert()
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

#Funcao que da pause
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
            if event.type == pygame.KEYDOWN:
                paused = False
        game_paused_img = pygame.image.load(path.join(cenarios_dir, "game_paused.png")).convert()
        game_paused_rect = game_paused_img.get_rect()
        screen.fill(BLACK)
        screen.blit(game_paused_img,game_paused_rect)
        pygame.display.flip()
        clock.tick(5)

#Funcao que aparece game over
def gameover(screen):
    gameover_img = pygame.image.load(path.join(cenarios_dir, "game_over.png")).convert()
    gameover_rect = gameover_img.get_rect()

    screen.fill(BLACK)
    screen.blit(gameover_img, gameover_rect)

    highscore = load_data()
    if score > highscore:
        highscore = score
        draw_text(screen, fontname, "New highscore! You got: "+str(highscore)+ "points", WIDTH/2, 10, BLUE)
        HS_FILE = "highscore.txt"
        with open((path.join(snr_dir, HS_FILE)) , 'w') as f:
            f.write(str(highscore))
    else:
        draw_text(screen, fontname, "Highscore: "+str(highscore)+ "points", 960, 10, BLACK)
        draw_text(screen, fontname, "Your score: "+str(score)+ "points", 340, 10, WHITE)

    pygame.display.flip()

    agora = pygame.time.get_ticks()

    waiting = True
    while waiting:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    waiting = False

        if (pygame.time.get_ticks() - agora) > 10000:
            waiting = False

#Funcao que le os scores
def load_data():
    HS_FILE = "highscore.txt"
    with open((path.join(snr_dir, HS_FILE)) , 'r') as f:
        try:
            highscore = int(f.read())
        except:
            highscore = 0
        return highscore

#----------------- SONS/IMAGENS/FONTES ------------------------------

# Fonte da letra usada no score e timer.
fontname = pygame.font.Font(path.join(fnt_dir, "Retron2000.ttf"),50)
font_size = 50
coracao = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"),50)

# Carrega os sons do jogo
pygame.mixer.music.load(path.join(snd_dir, 'kirby_star_ride.ogg'))
pygame.mixer.music.set_volume(0.4)

#Sons de colisao
hit_sound = pygame.mixer.Sound(path.join(snd_dir, 'hit_sound.ogg'))
hit_sound2 = pygame.mixer.Sound(path.join(snd_dir, 'hit_sound2.ogg'))

#Carrega as Imagens de Fundo e da plataforma de chao
fundo = pygame.image.load(path.join(cenarios_dir,'imagem_de_fundo.png')).convert()
fundo.set_colorkey(BLACK)
fundoX = 0
fundoX2 = fundo.get_width()
cenario_plataforma = pygame.image.load(path.join(cenarios_dir,'cenário_atual.png')).convert()
cenario_plataforma.set_colorkey(BLACK)
cenario_plataformaX = 0
cenario_plataformaX2 = cenario_plataforma.get_width()

#--------------- CRIAÇÃO DOS ELEMENTOS DO JOGO -------------------

#Cria o Kirby
player = Player()

# Cria um grupo de todos os sprites e adiciona o Kirby
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Cria as plataformas.
all_platforms = pygame.sprite.Group()
chao = Plataforma(0, HEIGHT - 150, 1280, 140) #Plataforma principal de chao
all_platforms.add(chao)
pygame.time.set_timer(USEREVENT+1, random.randrange(5000,20000)) #a cada 5 ate 20 segundos aparece uma plataforma voadora

#Cria os obstaculos
obstacles = pygame.sprite.Group()
pygame.time.set_timer(USEREVENT+2, random.randrange(1000,8000)) #a cada 1 ate 8 segundos ira aparecer obstaculos

#Cria os cogulemos de vida
all_cogumelos = pygame.sprite.Group()
pygame.time.set_timer(USEREVENT+3, random.randrange(25000,60000)) #a cada 25 ate 60 segundos ira aparecer obstaculos

#------------------------------------------------------------------

clock = pygame.time.Clock()

#Score do jogo
score = 0
lives = 3

pygame.mixer.music.play(loops=-1)

#------------------- LOOP PRINCIPAL ------------------------------
Menu() #Roda o Menu antes do jogo
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        #processar eventos do kirby (funcao dentro da classe player)
        player.process_event(event)
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        #Sair do jogo com ESC
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                quit()

        #Evento de pause no meio do jogo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause()

        #Eventos das plataformas
        if event.type == USEREVENT+1:
            r = random.randrange(0,2)
            if r == 0 or r == 1:
                p_voadora = Plataforma_voadora(random.randrange(640,1280),random.randrange(300, 400),200,70)
                all_platforms.add(p_voadora)
                all_sprites.add(p_voadora)

        #Eventos dos obstaculos
        if event.type == USEREVENT+2:
            r = random.randrange(0,2)
            if r == 0 or r == 1:
                new_obstacle = Obstaculo(1270, HEIGHT-300, 50, 50)
                obstacles.add(new_obstacle)
                all_sprites.add(new_obstacle)

        #Eventos dos cogumelos
        if event.type == USEREVENT+3:
            r = random.randrange(0,2)
            if r == 0 or r == 1:
                c_vida = Cogumelo(1270, HEIGHT-250, 100, 100)
                all_cogumelos.add(c_vida)
                all_sprites.add(c_vida)

    # Depois de processar os eventos.
    # Atualiza a acao de cada sprite.
    all_sprites.update()

    #--------------- COLISÕES ------------------
    hits_plataformas = pygame.sprite.spritecollide(player, all_platforms, False, pygame.sprite.collide_rect)
    if hits_plataformas:
        max_top = hits_plataformas[0].rect.top
        for p in hits_plataformas:
            top = p.rect.top
            bottom = p.rect.bottom
            if top > max_top:
                max_top = top

        player.speedy = 0
        player.rect.bottom = max_top

    # Verifica se houve colisao entre player e obstaculo
    hits_obstaculos = pygame.sprite.spritecollide(player, obstacles , False, pygame.sprite.collide_circle)
    if hits_obstaculos:
        hit_sound.play()
        lives-=1
        if lives == 0:
            running = False
            game_over = True

    # Verifica se houve colisao entre player e um sprite que dá mais vida
    hits_cogumelo = pygame.sprite.spritecollide(player, all_cogumelos, False, pygame.sprite.collide_circle)
    if hits_cogumelo:
        hit_sound2.play()
        lives+=1
    #----------------------------------------------------

    # A cada loop, redesenha o fundo e os sprites
    screen.fill(WHITE)
    redesenhafundo()
    all_sprites.draw(screen)

    score+=1
    #escreve o score na tela
    draw_text(screen, fontname, str(score), WIDTH/2, 10, BLACK)
    #mostra a vida na tela
    draw_text(screen, coracao, chr(9829)*lives, 200, 10, (255,0,0,10))

    # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()

    #-------------- PARAMETROS DOS FUNDOS ---------------------
    #Velocidade dos fundos
    if score <= 250:
        fundoX -= 12
        fundoX2 -= 12
        cenario_plataformaX -= 9
        cenario_plataformaX2 -= 9

    elif score <= 500:
        fundoX -= 15
        fundoX2 -= 15
        cenario_plataformaX -= 12
        cenario_plataformaX2 -= 12

    elif score <= 1250:
        fundoX -= 17
        fundoX2 -= 17
        cenario_plataformaX -= 15
        cenario_plataformaX2 -= 15

    elif score <= 1500:
        fundoX -= 20
        fundoX2 -= 20
        cenario_plataformaX -= 17
        cenario_plataformaX2 -= 17

    elif score <= 1750:
        fundoX -= 23
        fundoX2 -= 23
        cenario_plataformaX -= 20
        cenario_plataformaX2 -= 20

    elif score <= 2000:
        fundoX -= 26
        fundoX2 -= 26
        cenario_plataformaX -= 23
        cenario_plataformaX2 -= 23

    elif score <= 2250:
        fundoX -= 29
        fundoX2 -= 29
        cenario_plataformaX -= 26
        cenario_plataformaX2 -= 26

    elif score <= 2500:
        fundoX -= 32
        fundoX2 -= 32
        cenario_plataformaX -= 29
        cenario_plataformaX2 -= 29

    elif score <= 2750:
        fundoX -= 35
        fundoX2 -= 35
        cenario_plataformaX -= 32
        cenario_plataformaX2 -= 32

    elif score <= 3000:
        fundoX -= 38
        fundoX2 -= 38
        cenario_plataformaX -= 35
        cenario_plataformaX2 -= 35

    elif score <= 3250:
        fundoX -= 41
        fundoX2 -= 41
        cenario_plataformaX -= 38
        cenario_plataformaX2 -= 38

    #atualiza a localizacao dos fundos
    if fundoX < fundo.get_width() *-1:
        fundoX = fundo.get_width()

    if fundoX2 < fundo.get_width() *-1:
        fundoX2 = fundo.get_width()

    if cenario_plataformaX < cenario_plataforma.get_width() *-1:
        cenario_plataformaX = cenario_plataforma.get_width()

    if cenario_plataformaX2 < cenario_plataforma.get_width() *-1:
        cenario_plataformaX2 = cenario_plataforma.get_width()
    #------------------------------------------------------------

gameover(screen)
