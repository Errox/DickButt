import pygame
import time
import random

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
FPS = 30

# adding text
font = pygame.font.SysFont(None, 30)

#img
playerimg = pygame.image.load('player2.png')
sumo_ring = pygame.image.load('img/sumo_ring.png')


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(pygameScreen, color, [thingx, thingy, thingw, thingh])

def massage_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    pygameScreen.blit(screen_text, [200, HIGHT/2])

def player2(sumo_x, sumo_y):
    pygameScreen.blit(playerimg, (sumo_x, sumo_y))
    pygame.display.update()

def sumo_ring(backroundx, backroundy):
    pygameScreen.blit(playerimg, (900, 900))
    pygame.display.update()



def gameLoop():
    gameExit = False
    gameOver = False

    #objects  player 
    sumo_x = WIDTH/2   
    sumo_y = 500

    sumo_x_change = 0
    sumo_y_change = 0  

    #enemy player
    #enemy_x = round(random.randrange(0, WIDTH-block_size)/10.0)*10.0 
    #enemy_y = round(random.randrange(0, HIGHT-block_size)/10.0)*10.0 

    thing_startx = random.randrange(0, WIDTH)
    thing_starty = -600
    thing_speed = 15
    thing_width = 30
    thing_height = 30

    while not gameExit:
        
        while gameOver == True:
            pygameScreen.fill(WHITE)
            massage_to_screen("GAME OVER, C = replay  Q = quit", BLUE)
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

           
            #if sumo_x == enemy_x or sumo_y == enemy_y:
                    #gameOver = True  

            #if event.type == pygame.KEYUP:
                #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    #sumo_x_change = 0          
            

            # dit moet gebeuren met Y want als je ervan af valt is het game over
            if sumo_x >= 900 or sumo_x <= 0 or sumo_y >= 900 or sumo_y <= 0:
                gameOver = True 
                
            
            
            
        sumo_x += sumo_x_change  
        sumo_y += sumo_y_change  
        pygameScreen.fill(WHITE)
        #pygame.draw.rect(pygameScreen, GREEN,[enemy_x, enemy_y, 30, 30])
        
        
        things(thing_startx, thing_starty, thing_width, thing_height, GREEN)
        thing_starty += thing_speed
        player2(sumo_x, sumo_y)


        if thing_starty > HIGHT:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,WIDTH)


        pygame.display.update()

        clock.tick(FPS)


    
    pygame.quit()
    quit()

gameLoop()
