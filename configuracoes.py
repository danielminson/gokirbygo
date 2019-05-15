from os import path

WIDTH, HEIGHT = 1280, 720

size = [1280, 720]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Diretorios de imagens
img_dir = path.join(path.dirname(__file__), 'Imagens')
cenarios_dir = path.join(path.dirname(__file__), 'Imagens', 'cenario')

CHAO = 0
JUMP = 1

FPS = 100

INIT = 0
GAME = 1
QUIT = 2
