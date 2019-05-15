import pygame
import random
from os import path

from configuracoes import cenarios_dir, BLACK, FPS, GAME, QUIT

def Menu(screen):

    clock = pygame.time.Clock()

    #Converte a imagem de menu
    menu_img = pygame.image.load(path.join(cenarios_dir, "entrada_v1.png")).convert()
    menu_rect = menu_img.get_rect()

    intro = True
    while intro:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                intro = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    state = GAME
                    intro = False

        screen.fill(BLACK)
        screen.blit(menu_img,menu_rect)
        pygame.display.flip()
    return state
