import pygame
import random
import time

from os import path

from configuracoes import WIDTH, HEIGHT, INIT, GAME, QUIT
from menu import Menu
from sprites import game

pygame.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Go Kirby Go")

# Comando para evitar travamentos.
try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = Menu(screen)
        elif state == GAME:
            state = game(screen)
        else:
            state = QUIT
finally:
    pygame.quit()
