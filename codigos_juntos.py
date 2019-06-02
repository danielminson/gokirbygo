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
cenarios_dir = path.join(path.dirname(__file__), 'Imagens', 'Imagens_Fundo')
obs_dir = path.join(path.dirname(__file__), 'Imagens', 'Obstaculos')
snr_dir = path.join(path.dirname(__file__))
snd_dir = path.join(path.dirname(__file__), "Som")
fnt_dir = path.join(path.dirname(__file__), 'Fontes')
kirby_dir = path.join(path.dirname(__file__), 'Imagens', 'Kirby') #kirby andando
k_dir = path.join(path.dirname(__file__),"Imagens","Kirby_voando") # kirby voando
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

        self.image = pygame.image.load(path.join(cenarios_dir, "plataforma_voadora.png")).convert()
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
def redesenhafundo(fundo,fundoX,fundoX2,chao,chaoX,chaoX2):
    screen.blit(fundo, (fundoX, 0))
    screen.blit(fundo, (fundoX2, 0))
    screen.blit(chao, (chaoX, 0))
    screen.blit(chao, (chaoX2, 0))
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
    vaicontinuar = False
    while waiting and vaicontinuar==False:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    waiting = False
                    vaicontinuar = True

        if (pygame.time.get_ticks() - agora) > 10000:
        #    waiting = False
            return False
    if vaicontinuar:
        return True

#Funcao que le os scores
def load_data():
    HS_FILE = "highscore.txt"
    try:
        with open((path.join(snr_dir, HS_FILE)) , 'r') as f:
            highscore = int(f.read())
    except:
        with open((path.join(snr_dir, HS_FILE)) , 'w') as f:
            highscore = 0
            f.write(str(highscore))
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

#Cenário 1 -----------------------------------------------------------------------------
fundo_score1 = pygame.image.load(path.join(cenarios_dir,'imagem_de_fundoe.png')).convert()
fundo_score1.set_colorkey(BLACK)
fundoX_score1 = 0
fundoX2_score1 = fundo_score1.get_width()

chao_grama = pygame.image.load(path.join(cenarios_dir,'chao.png')).convert()
chao_grama.set_colorkey(BLACK)
chao_gramaX = 0
chao_gramaX2 = chao_grama.get_width()

#Cenário 2 ------------------------------------------------------------------------------
fundo_score2 = pygame.image.load(path.join(cenarios_dir,'imagem_de_fundo2.png')).convert()
fundo_score2.set_colorkey(BLACK)
fundoX_score2 = 0
fundoX2_score2 = fundo_score2.get_width()

chao_nuvem = pygame.image.load(path.join(cenarios_dir,'chao2.png')).convert()
chao_nuvem.set_colorkey(BLACK)
chao_nuvemX = 0
chao_nuvemX2 = chao_nuvem.get_width()

#Cenário 3 ------------------------------------------------------------------------------
fundo_score3 = pygame.image.load(path.join(cenarios_dir,'imagem_de_fundo3.png')).convert()
fundo_score3.set_colorkey(BLACK)
fundoX_score3 = 0
fundoX2_score3 = fundo_score3.get_width()

chao_arcoiris = pygame.image.load(path.join(cenarios_dir,'chao3.png')).convert()
chao_arcoiris.set_colorkey(BLACK)
chao_arcoirisX = 0
chao_arcoirisX2 = chao_arcoiris.get_width()

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
pygame.time.set_timer(USEREVENT+2, random.randrange(1000,5000)) #a cada 1 ate 8 segundos ira aparecer obstaculos

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


    if score % 250 == 0:
        for x in obstacles:
            x.vel += 2

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
            running = gameover(screen)
            lives=3
            score=0
            if running== False:
                pygame.quit()
                quit()

    # Verifica se houve colisao entre player e um sprite que dá mais vida
    hits_cogumelo = pygame.sprite.spritecollide(player, all_cogumelos, False, pygame.sprite.collide_circle)
    if hits_cogumelo:
        if lives < 3:
            hit_sound2.play()
            lives+=1
    #----------------------------------------------------

    # A cada loop, redesenha o fundo e os sprites
    screen.fill(WHITE)

    score+=1

    if score <= 1000:
        redesenhafundo(fundo_score1,fundoX_score1,fundoX2_score1,
        chao_grama,chao_gramaX,chao_gramaX2)

    if 1000 < score <= 2000:
        redesenhafundo(fundo_score2,fundoX_score2,fundoX2_score2,
        chao_nuvem,chao_nuvemX,chao_nuvemX2)

    if 2000 < score:
        redesenhafundo(fundo_score3,fundoX_score3,fundoX2_score3,
        chao_arcoiris,chao_arcoirisX,chao_arcoirisX2)

    all_sprites.draw(screen)

    #escreve o score na tela
    draw_text(screen, fontname, str(score), WIDTH/2, 10, BLACK)
    #mostra a vida na tela
    draw_text(screen, coracao, chr(9829)*lives, 200, 10, (255,0,0,10))

    # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()

    #-------------- PARAMETROS DOS FUNDOS ---------------------

    #Velocidade dos fundos a cada score
    if score <= 250:

        fundoX_score1 -= 12
        fundoX2_score1 -= 12
        fundoX_score2 -= 12
        fundoX2_score2 -= 12
        fundoX_score3 -= 12
        fundoX2_score3 -= 12

        chao_gramaX -= 9
        chao_gramaX2 -= 9
        chao_nuvemX -= 9
        chao_nuvemX2 -= 9
        chao_arcoirisX -= 9
        chao_arcoirisX2 -= 9

    elif score <= 500:

        fundoX_score1 -= 15
        fundoX2_score1 -= 15
        fundoX_score2 -= 15
        fundoX2_score2 -= 15
        fundoX_score3 -= 15
        fundoX2_score3 -= 15

        chao_gramaX -= 12
        chao_gramaX2 -= 12
        chao_nuvemX -= 12
        chao_nuvemX2 -= 12
        chao_arcoirisX -= 12
        chao_arcoirisX2 -= 12


    elif score <= 1000:

        fundoX_score1 -= 17
        fundoX2_score1 -= 17
        fundoX_score2 -= 17
        fundoX2_score2 -= 17
        fundoX_score3 -= 17
        fundoX2_score3 -= 17

        chao_gramaX -= 15
        chao_gramaX2 -= 15
        chao_nuvemX -= 15
        chao_nuvemX2 -= 15
        chao_arcoirisX -= 15
        chao_arcoirisX2 -= 15

    elif score <= 1250:

        fundoX_score1 -= 20
        fundoX2_score1 -= 20
        fundoX_score2 -= 20
        fundoX2_score2 -= 20
        fundoX_score3 -= 20
        fundoX2_score3 -= 20

        chao_gramaX -= 18
        chao_gramaX2 -= 18
        chao_nuvemX -= 18
        chao_nuvemX2 -= 18
        chao_arcoirisX -= 18
        chao_arcoirisX2 -= 18

    elif score <= 1500:

        fundoX_score1 -= 23
        fundoX2_score1 -= 23
        fundoX_score2 -= 23
        fundoX2_score2 -= 23
        fundoX_score3 -= 23
        fundoX2_score3 -= 23

        chao_gramaX -= 21
        chao_gramaX2 -= 21
        chao_nuvemX -= 21
        chao_nuvemX2 -= 21
        chao_arcoirisX -= 21
        chao_arcoirisX2 -= 21

    elif score <= 1750:

        fundoX_score1 -= 26
        fundoX2_score1 -= 26
        fundoX_score2 -= 26
        fundoX2_score2 -= 26
        fundoX_score3 -= 26
        fundoX2_score3 -= 26

        chao_gramaX -= 24
        chao_gramaX2 -= 24
        chao_nuvemX -= 24
        chao_nuvemX2 -= 24
        chao_arcoirisX -= 24
        chao_arcoirisX2 -= 24

    elif score <= 2000:

        fundoX_score1 -= 29
        fundoX2_score1 -= 29
        fundoX_score2 -= 29
        fundoX2_score2 -= 29
        fundoX_score3 -= 29
        fundoX2_score3 -= 29

        chao_gramaX -= 27
        chao_gramaX2 -= 27
        chao_nuvemX -= 27
        chao_nuvemX2 -= 27
        chao_arcoirisX -= 27
        chao_arcoirisX2 -= 27

    elif score <= 2250:

        fundoX_score1 -= 32
        fundoX2_score1 -= 32
        fundoX_score2 -= 32
        fundoX2_score2 -= 32
        fundoX_score3 -= 32
        fundoX2_score3 -= 32

        chao_gramaX -= 30
        chao_gramaX2 -= 30
        chao_nuvemX -= 30
        chao_nuvemX2 -= 30
        chao_arcoirisX -= 30
        chao_arcoirisX2 -= 30

    elif score <= 2500:

        fundoX_score1 -= 35
        fundoX2_score1 -= 35
        fundoX_score2 -= 35
        fundoX2_score2 -= 35
        fundoX_score3 -= 35
        fundoX2_score3 -= 35

        chao_gramaX -= 33
        chao_gramaX2 -= 33
        chao_nuvemX -= 33
        chao_nuvemX2 -= 33
        chao_arcoirisX -= 33
        chao_arcoirisX2 -= 33

    elif score <= 2750:

        fundoX_score1 -= 38
        fundoX2_score1 -= 38
        fundoX_score2 -= 38
        fundoX2_score2 -= 38
        fundoX_score3 -= 38
        fundoX2_score3 -= 38

        chao_gramaX -= 36
        chao_gramaX2 -= 36
        chao_nuvemX -= 36
        chao_nuvemX2 -= 36
        chao_arcoirisX -= 36
        chao_arcoirisX2 -= 36

    elif score <= 100000:

        fundoX_score1 -= 41
        fundoX2_score1 -= 41
        fundoX_score2 -= 41
        fundoX2_score2 -= 41
        fundoX_score3 -= 41
        fundoX2_score3 -= 41

        chao_gramaX -= 39
        chao_gramaX2 -= 39
        chao_nuvemX -= 39
        chao_nuvemX2 -= 39
        chao_arcoirisX -= 39
        chao_arcoirisX2 -= 39

    #Atualiza a localizacao dos fundos

    #Cenário 1--------------------------------------------------------------------
    if fundoX_score1 < fundo_score1.get_width() *-1:
        fundoX_score1 = fundo_score1.get_width()

    if fundoX2_score1 < fundo_score1.get_width() *-1:
        fundoX2_score1 = fundo_score1.get_width()

    if chao_gramaX < chao_grama.get_width() *-1:
        chao_gramaX = chao_grama.get_width()

    if chao_gramaX2 < chao_grama.get_width() *-1:
        chao_gramaX2 = chao_grama.get_width()

    #Cenário 2 -------------------------------------------------------------------
    if fundoX_score2 < fundo_score2.get_width() *-1:
        fundoX_score2 = fundo_score2.get_width()

    if fundoX2_score2 < fundo_score2.get_width() *-1:
        fundoX2_score2 = fundo_score2.get_width()

    if chao_nuvemX < chao_nuvem.get_width() *-1:
        chao_nuvemX = chao_nuvem.get_width()

    if chao_nuvemX2 < chao_nuvem.get_width() *-1:
        chao_nuvemX2 = chao_nuvem.get_width()

    #Cenário 3 -------------------------------------------------------------------
    if fundoX_score3 < fundo_score3.get_width() *-1:
        fundoX_score3 = fundo_score3.get_width()

    if fundoX2_score3 < fundo_score3.get_width() *-1:
        fundoX2_score3 = fundo_score3.get_width()

    if chao_arcoirisX < chao_arcoiris.get_width() *-1:
        chao_arcoirisX = chao_arcoiris.get_width()

    if chao_arcoirisX2 < chao_arcoiris.get_width() *-1:
        chao_arcoirisX2 = chao_arcoiris.get_width()

#------------------------------------------------------------

gameover(screen)
