import pygame
import time

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

#differnt blocks
block_size = 10
block_player = 30

# FPS Clock
clock= pygame.time.Clock()

# adding text
font = pygame.font.SysFont(None, 30)



def massage_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    pygameScreen.blit(screen_text, [200, HIGHT/2])

def gameLoop():
    gameExit = False
    gameOver = False

    #objects  player 
    sumo_x = WIDTH/2   
    sumo_y = 500

    sumo_x_change = 0
    sumo_y_change = 0  

    """enemy player
    enemy_playerx = random.randrange
    enemy_playery """

    while not gameExit:
        
        while gameOver == True:
            pygameScreen.fill(WHITE)
            massage_to_screen("lol you lost, press c to play again press q to quit", BLUE)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sumo_x_change = -block_size
                    sumo_y_change = 0
                if event.key == pygame.K_RIGHT:   
                    sumo_x_change = block_size  
                    sumo_y_change = 0
                if event.key == pygame.K_UP:
                    sumo_y_change = -block_size
                    sumo_x_change = 0
                if event.key == pygame.K_DOWN:   
                    sumo_y_change = block_size  
                    sumo_x_change = 0
            
            #if event.type == pygame.KEYUP:
                #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    #sumo_x_change = 0          
            

            # dit moet gebeuren met Y want als je ervan af valt is het game over
            if sumo_x >= WIDTH or sumo_x <= 0 or sumo_y >= HIGHT or sumo_y <= 0:
                gameOver = True 
                
            
            
            
        sumo_x += sumo_x_change  
        sumo_y += sumo_y_change  
        pygameScreen.fill(WHITE)    
        pygame.draw.rect(pygameScreen, PURPLE,[sumo_x, sumo_y, 30, 30])
        pygame.draw.rect(pygameScreen, GREEN,[WIDTH/2, 300, 30, 30])
        pygame.display.update()

        clock.tick(30)

    """massage_to_screen("you lost ... soooo byyeeee", RED)
    pygame.display.update() 
    time.sleep(1)"""
    pygame.quit()
    quit()

gameLoop()
