def redesenhafundo():
    screen.blit(fundo, (fundoX, 0)) 
    screen.blit(fundo, (fundoX2, 0))  
    pygame.display.update()


fundo = pygame.image.load(path.join('Imagens','cenário_atual.png')).convert()
fundoX = 0
fundoX2 = fundo.get_width()

#Cria o Kirby
player = Player()
# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
speed = 60  

while running:

    for event in pygame.event.get(): 
        player.process_event(event) 
        if event.type == pygame.QUIT: 
            running = False    
            pygame.quit() 
            quit()
    # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.


    all_sprites.update()

    # A cada loop, redesenha o fundo e os sprites
    screen.fill(black)
    redesenhafundo()
    all_sprites.draw(screen)
    
    # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()

    fundoX -= 5
    fundoX2 -= 5

    if fundoX < fundo.get_width() * -1:  
        fundoX = fundo.get_width()
    
    if fundoX2 < fundo.get_width() * -1:
        fundoX2 = fundo.get_width()


    clock.tick(speed) 