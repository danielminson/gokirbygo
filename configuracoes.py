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
png_dir = path.join(path.dirname(__file__), 'Imagens', 'png')
bos_dir = path.join(path.dirname(__file__), 'Imagens', 'boss')
plat_dir = path.join(path.dirname(__file__), 'Imagens', 'plataforma')
obs_dir = path.join(path.dirname(__file__), 'Imagens', 'obstaculo')

CHAO = 0
JUMP = 1

FPS = 100

INIT = 0
GAME = 1
QUIT = 2
