import pygame
from pygame.locals import *
import os
import sys
import math

pygame.init()

W, H = 1200, 700
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption('Go Kirby Go')

bg = pygame.image.load(os.path.join('Imagens','cenário_atual.png')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

def redrawWindow():
    screen.blit(bg, (bgX, 0))  # draws our first bg image
    screen.blit(bg, (bgX2, 0))  # draws the seconf bg image
    pygame.display.update()  # updates the screen

run = True
speed = 30  

while run:
    redrawWindow() 
    bgX -= 1.4  
    bgX2 -= 1.4

    if bgX < bg.get_width() * -1:  
        bgX = bg.get_width()
    
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False    
            pygame.quit() 
            quit()
    
        if event.type == USEREVENT+1: # Checks if timer goes off
            speed += 1 # Increases speed

    clock.tick(speed) 