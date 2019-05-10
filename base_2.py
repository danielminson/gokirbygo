import pygame, random, sys
pygame.init()
global screen, size, background, state, mainState, jumpState
from time import sleep 
from os import path

mainState = 0
jumpState = 1
slideState = 2
size = [1280, 720]
white = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
screen = pygame.display.set_mode(size)
img_dir = path.join(path.dirname(__file__), 'imagens')

class Player_Kirby(pygame.sprite.Sprite):
    def __init__(self, screen):

        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(path.join(img_dir, "kirby.png")).convert()
        self.image = player_img
        self.image = pygame.transform.scale(player_img, (100, 100))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.posX, self.posY = 50, size[1] - 180
        self.rect.center = (self.posX, self.posY)
        self.jumpSpeed = 10
        self.cairSpeed = 11
        self.slideDis = 4
        
    def jump(self):
        self.rect.centery -= self.jumpSpeed

    def cair(self):   
        self.rect.centery += self.cairSpeed
    
    def estado_parado(self):
         self.rect.center = self.rect.center
     
class Ground (pygame.sprite.Sprite):
    def __init__(self, screen):
        color = BLACK
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size[0], size[0]))
        rect = pygame.Rect(20, 20, 20, 20)
        pygame.draw.rect(self.image, color, rect, 1)
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.rect.center = (size[0] / 2 , size[1] + 250)

class Obstacle (pygame.sprite.Sprite):
    def __init__(self, screen):
        color = BLACK
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        rect = pygame.Rect(20, 20, 20, 20)
        pygame.draw.rect(self.image, color, rect, 1)
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.posX, self.posY = size[0] + 30, 438
        self.maxPosX = self.posX * 2
        self.rect.center = (self.posX, self.posY)
        self.speed = 20
        
    def update(self):
        self.rect.centerx -= self.speed

    def reset(self):
        obPlace = random.randint(0,1)
        if obPlace == 0:
            self.rect.center = (random.randint(self.posX, self.maxPosX), self.posY)
        else:
            self.rect.center = (random.randint(self.posX, self.maxPosX), self.posY - 30)

def load_assets(img_dir):
    assets = {}
    assets["foto_kirby"] = pygame.image.load(path.join(img_dir, "kirby.png")).convert()
    assets["fundo"] = pygame.image.load(path.join(img_dir, "cenario1_teste.png")).convert()
    return assets           
def main():
    state = mainState
    score = 0
    screen = pygame.display.set_mode(size)           
    pygame.display.set_caption("Run")  
  
    background = pygame.Surface(screen.get_size())  
    background = background.convert()              
    background.fill(white)

    clock = pygame.time.Clock()    
    timeElapsed = 0
    timeReset = 0

    player = Player_Kirby(screen)
    groundSprite = Ground(screen)
    obstacleSprite = Obstacle(screen)

    groundSprite.rect.top = player.rect.bottom
    
    allSprites = pygame.sprite.Group(player, groundSprite, obstacleSprite)
    
    keepGoing = True
    while keepGoing:
        
        clockTime = clock.tick(60)
        timeElapsed += clockTime
        timeSec = timeElapsed / 1000
        timeElapsed += clockTime

        scoreText = "Score: " +str(score)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                quit()
            elif event.type == pygame.KEYDOWN:
                if state == mainState:
                    if event.key == pygame.K_SPACE:
                        state = jumpState
                        timeReset = 0
                    if event.key == pygame.K_s:
                        state = slideState
                        timeReset = 0
            
        if state == jumpState and timeReset < 5:
            player.jump()
            timeReset += 1
        elif state == jumpState and timeReset < 7:
            player.estado_parado()
            timeReset += 1
        elif state == jumpState and timeReset < 11:
            player.cair()
            player.cairSpeed += 1
            timeReset += 1
        elif state == slideState and timeReset <10:
            player.slide()
            timeReset += 1
        else:
            player.reset()
            player.cairSpeed = 11
            state = mainState

        guyCollide = pygame.sprite.collide_rect(player, obstacleSprite)
        if guyCollide:
            keepGoing = False
        if obstacleSprite.rect.right < 0:
            obstacleSprite.reset()
            score += 1
        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        font=pygame.font.Font(None,30)
        scoretext=font.render(scoreText, 1 , (BLACK))
        screen.blit(scoretext, (10 , 10))
   
        pygame.display.flip()
        screen.blit(background, (0,0))
        
    gameOver(score)
    
def intro():
    state = mainState
    background = pygame.Surface(screen.get_size())  
    background = background.convert()              
    background.fill(white)
    screen.blit(background, (0, 0))

    clock = pygame.time.Clock()

    player = Player_Kirby(screen)
    groundSprite = Ground(screen)

    groundSprite.rect.top = player.rect.bottom

    allSprites = pygame.sprite.Group(player, groundSprite)
    
    pygame.mouse.set_visible(False)
    
    keepGoing = True
    while keepGoing:
        
        clockTime = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        keepGoing = False                
        
        introString = []
        introString.append("Don't get hit by the block")
        introString.append("Press 'space' to jump")
        introString.append("Press 's' to slide")
        introString.append("Press 'space' to continue")
        i = 0
        ix = 100
        for i in range(len(introString)):
            font=pygame.font.Font(None,30)
            introText=font.render(introString[i], 1 , (BLACK))
            screen.blit(introText, ((size[0] / 2) - 130 , size[1] / 2 - ix))
            i += 1
            ix -= 25
            
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()

def gameOver(score):
    background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
    background_rect = background.get_rect()
    background.fill(white)
    screen.blit(background, (0, 0))

    clock = pygame.time.Clock()

    groundSprite = Ground(screen)

    allSprites = pygame.sprite.Group(groundSprite)
    
    pygame.mouse.set_visible(False)
    
    keepGoing = True
    while keepGoing:
        
        clockTime = clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        keepGoing = False                
        
        introString = []
        introString.append("You Died")
        introString.append("Your score was " +str(score))
        introString.append("Press 'space' to continue")
        i = 0
        ix = 100
        for i in range(len(introString)):
            font=pygame.font.Font(None,30)
            introText=font.render(introString[i], 1 , (BLACK))
            screen.blit(introText, ((size[0] / 2) - 130 , size[1] / 2 - ix))
            i += 1
            ix -= 25


        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
        
    main()
    
def quit():
    pygame.display.quit()
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    intro()
    main()