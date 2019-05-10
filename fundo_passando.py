import pygame
from pygame.locals import *
import os
import sys
import math

pygame.init()

W, H = 1440, 800
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption('Go Kirby Go')

fundo = pygame.image.load(os.path.join('Imagens','cenário_atual.png')).convert()
fundoX = 0
fundoX2 = fundo.get_width()

clock = pygame.time.Clock()

def redesenhafundo():
    screen.blit(fundo, (fundoX, 0)) 
    screen.blit(fundo, (fundoX2, 0))  
    pygame.display.update()

running = True
speed = 60  

while running:
    redesenhafundo() 
    fundoX -= 5
    fundoX2 -= 5

    if fundoX < fundo.get_width() * -1:  
        fundoX = fundo.get_width()
    
    if fundoX2 < fundo.get_width() * -1:
        fundoX2 = fundo.get_width()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False    
            pygame.quit() 
            quit()

    clock.tick(speed) 