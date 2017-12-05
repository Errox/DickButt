import pygame

pygame.init()


#Color coding 
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
RED = (225, 0, 0)
BLUE = (0, 0, 255 )
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)

#difine game core
WIDTH = 900
HIGHT = 900

pygameScreen = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption('SUMO SMASH')


gameExit = False

#objects  player =
sumo_x = WIDTH/2    # lead_x
sumo_y = 500

#blocks
block_size = 30

# FPS Clock
clock= pygame.time.Clock()


#My main loop
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sumo_x -= 100
            if event.key == pygame.K_RIGHT:   
                sumo_x += 100   

        # dit moet gebeuren met Y want als je ervan af valt is het game over
        if sumo_x > 900 or sumo_x < 0:
            gameExit = True
        
        
        
        
    pygameScreen.fill(WHITE)    
    pygame.draw.rect(pygameScreen, PURPLE,[sumo_x, sumo_y, 30, 30])
    pygame.draw.rect(pygameScreen, GREEN,[WIDTH/2, 300, 30, 30])
    pygame.display.update()

    clock.tick(30)

    
    


    