#import all lib's
import pygame
import random
import os

#define pygame core
WIDTH   = 900
HEIGHT  = 900
FPS     = 60
X       = 500
Y       = 100

#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#set x and y of the window on screen. (EXPIRIMENTAL)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
#initiate pygame itself
pygame.init() 
#init the sound libs of pygame.
pygame.mixer.init()
pygame.mixer.music.load("res/music/main_menu_music.mp3")
pygame.mixer.music.play(-1)
#set height and width of the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#Set caption
pygame.display.set_caption("First stage")
#set FTP rate of clock ticks. 
clock = pygame.time.Clock()


#game loop
running = True
while running:
    # keep loop running at the right fps
    clock.tick(FPS)

    #process input (events)
    for event in pygame.event.get():
        #check for closing the windows
        if event.type == pygame.QUIT:
            #if the close button is pressed, the game will close
            running = False

    #update 

    #draw / render
    screen.fill(BLACK)
    #After drawing everything, flip the display.
    pygame.display.flip()

pygame.quit()