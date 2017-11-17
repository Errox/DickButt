#this python script is a boilerplate for everyone to use and learn about pygame. 
# @To-do
# - Make a sprite example
# - Make a menu example
# - Make the usage of sounds example 


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

#set height and width of the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Set caption
pygame.display.set_caption("Core version, template made for everyone to learn and get a basic core")

#set FTP rate of clock ticks. 
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()

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
    all_sprites.update()

    #draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #After drawing everything, flip the display.
    pygame.display.flip()

pygame.quit()