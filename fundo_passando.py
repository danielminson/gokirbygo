import pygame
from pygame.locals import *
import os
import sys
import math

pygame.init()

W, H = 1280, 720
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption('Go Kirby Go')

fundo = pygame.image.load(os.path.join('Imagens','cenário_atual.png')).convert()
fundoX = 0
fundoX2 = bg.get_width()

clock = pygame.time.Clock()

def redesenhafundo():
    screen.blit(fundo, (fundoX, 0))  # draws our first bg image
    screen.blit(fundo, (fundoX2, 0))  # draws the seconf bg image
    pygame.display.update()  # updates the screen

running = True
speed = 30  

while running:
    redesenhafundo() 
    fundoX -= 1.4  
    fundoX2 -= 1.4

    if fundoX < fundo.get_width() * -1:  
        fundoX = fundo.get_width()
    
    if fundoX2 < fundo.get_width() * -1:
        fundoX2 = fundo.get_width()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False    
            pygame.quit() 
            quit()
    
        if event.type == USEREVENT+1: # Checks if timer goes off
            speed += 1 # Increases speed

    clock.tick(speed) 