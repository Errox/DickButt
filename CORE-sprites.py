#This script is for playing and moving around a sprite
#import all lib's
import pygame
import random
import os

#define pygame core
WIDTH   = 900
HEIGHT  = 900
FPS     = 30
X       = 500
Y       = 100

#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class player(pygame.sprite.Sprite):
    #sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.Surface((50, 50))
        
        self.image  = pygame.image.load("res/images/NPC_35.png")
        # self.image.fill(GREEN)
        self.rect   = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0



class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#set x and y of the window on screen. (EXPIRIMENTAL)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)

#initiate pygame itself
pygame.init() 

#init the sound libs of pygame.
pygame.mixer.init()
pygame.mixer.music.load("res/music/main_menu.ogg")
pygame.mixer.music.play(-1)

#set height and width of the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Set caption
pygame.display.set_caption("First stage")

#set FTP rate of clock ticks. 
clock = pygame.time.Clock()

BackGround = Background('res/backgrounds/Background_94.png', [0,300])
all_sprites = pygame.sprite.Group()
player = player()
all_sprites.add(player)

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
    screen.blit(BackGround.image, BackGround.rect)
    all_sprites.draw(screen)
    #After drawing everything, flip the display.
    pygame.display.flip()

pygame.quit()