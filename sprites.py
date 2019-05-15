import pygame
import random
from os import path

from configuracoes import img_dir, cenarios_dir, WIDTH, HEIGHT, BLACK, YELLOW, RED, FPS, QUIT, CHAO, JUMP, WHITE

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

def redesenhafundo(screen):
    fundo = pygame.image.load(path.join(cenarios_dir,'imagem_de_fundo.png')).convert()
    fundo.set_colorkey(BLACK)
    fundoX = 0
    fundoX2 = fundo.get_width()

    cenario_plataforma = pygame.image.load(path.join(cenarios_dir,'cenário_atual.png')).convert()
    cenario_plataforma.set_colorkey(BLACK)
    cenario_plataformaX = 0
    cenario_plataformaX2 = cenario_plataforma.get_width()

    screen.blit(fundo, (fundoX, 0))
    screen.blit(fundo, (fundoX2, 0))
    screen.blit(cenario_plataforma, (cenario_plataformaX, 0))
    screen.blit(cenario_plataforma, (cenario_plataformaX2, 0))
    pygame.display.update()

def draw_text(surface, text, font_size, x, y, color):
    fontname = pygame.font.match_font("arial")  # Fonte da letra usada no score e timer.
    font_size = 50
    font = pygame.font.Font(fontname, font_size)
    text_surface = font.render(text, True, color)
    text_rect=text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def game(screen):
    
    clock = pygame.time.Clock()

    #Cria o Kirby
    player = Player()

    # Cria um grupo de todos os sprites e adiciona a nave.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Cria as plataformas.
    all_platforms = pygame.sprite.Group()

    #Plataforma principal de chao
    chao = Plataforma(0, HEIGHT - 140, 1280, 150)
    all_platforms.add(chao)

    PLAYING = 0
    DONE = 1
    lives = 3
    score = 0

    fundo = pygame.image.load(path.join(cenarios_dir,'imagem_de_fundo.png')).convert()
    fundo.set_colorkey(BLACK)
    fundoX = 0
    fundoX2 = fundo.get_width()

    cenario_plataforma = pygame.image.load(path.join(cenarios_dir,'cenário_atual.png')).convert()
    cenario_plataforma.set_colorkey(BLACK)
    cenario_plataformaX = 0
    cenario_plataformaX2 = cenario_plataforma.get_width()

    state = PLAYING
    while state != DONE:
        if state == PLAYING:

            for event in pygame.event.get():
                player.process_event(event)

                if event.type == pygame.QUIT:
                    state = DONE

        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()

        if state == PLAYING:
            # Verifica se houve colisão entre nave e meteoro
            hits = pygame.sprite.spritecollide(player, all_platforms, False, pygame.sprite.collide_rect)
            if hits:
                # Toca o som da colisão
                player.estado = CHAO
                player.speedy = 0

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(WHITE)
        redesenhafundo(screen)
        all_sprites.draw(screen)

        fontname = pygame.font.match_font("arial")  # Fonte da letra usada no score e timer.
        font_size = 50
        draw_text(screen, chr(9829)* lives, 100, 200, 0, RED)
        score+=1
        #escreve o score na tela
        draw_text(screen, str(score), font_size, WIDTH/2, 10, BLACK)

        #mostra a vida na tela
        draw_text(screen, chr(9829)*lives, 100, 200, 0, RED)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        #Velocidade dos fundos
        fundoX -= 5
        fundoX2 -= 5
        cenario_plataformaX -= 5
        cenario_plataformaX2 -= 5

        if fundoX < fundo.get_width() *-1:
            fundoX = fundo.get_width()

        if fundoX2 < fundo.get_width() *-1:
            fundoX2 = fundo.get_width()

        if cenario_plataformaX < cenario_plataforma.get_width() *-1:
            cenario_plataformaX = cenario_plataforma.get_width()

        if cenario_plataformaX2 < cenario_plataforma.get_width() *-1:
            cenario_plataformaX2 = cenario_plataforma.get_width()


    clock.tick(FPS)

    return QUIT
