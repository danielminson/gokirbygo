import pygame
from pygame.locals import *
from os import path
import sys 
import math

W, H = 800, 447
win = pygame.display.set_mode((W,H))
FPS = 30
img_dir = path.join(path.dirname(__file__), 'Imagens')

def redrawWindow():
    win.blit(fundo, (fundoX, 0))
    win.blit(fundo, (fundoX2, 0))  
    pygame.display.update() 
 
def load_assets(img_dir):
	assets = {}
	assets["fundo"] = pygame.image.load(path.join(img_dir,"cenario1_teste.png")).convert()
	return assets

pygame.init()

screen = pygame.display.set_mode((W, H))

pygame.display.set_caption('Go Kirby Go')

clock = pygame.time.Clock()

assets = load_assets(img_dir)
fundo = assets["fundo"]
fundoX = 0
fundoX2 = fundo.get_width()

# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        fundoX -= 1.4
        fundoX2 -= 1.4

        if fundoX < fundo.get_width() * -1:
        	fundoX = fundo.get_width()
        if fundoX2 < fundo.get_width() * -1:
        	fundoX2 = fundo.get_width()
       
        
finally:
    pygame.quit()