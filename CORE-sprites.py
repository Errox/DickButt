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
size = [200, 200]
bg = [255, 255, 255]

# set up assets
game_folder = os.path.dirname(__file__)
img_folder  = os.path.join(game_folder, "img")

button = pygame.Rect(100, 100, 50, 50)
class player(pygame.sprite.Sprite):
    #sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.Surface((50, 50))
        
        self.image  = pygame.image.load(os.path.join(img_folder, "NPC_35.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect   = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.bottom > HEIGHT - 150:
            self.y_speed = -5
        if self.rect.top < 150:
            self.y_speed = 5
              

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
# pygame.mixer.music.load("music/main_menu.ogg")
# pygame.mixer.Sound.play(-1)

#set height and width of the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Set caption
pygame.display.set_caption("First stage")

#set FTP rate of clock ticks. 
clock = pygame.time.Clock()

BackGround = Background('img/backgrounds/Background_94.png', [0,300])
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
        if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() # gets mouse position

                # checks if mouse position is over the button
                # note this method is constantly looking for collisions
                # the only reason you dont see an evet activated when you
                #hover over the button is because the method is bellow the
                # mousedown event if it were outside it would be called the
                # the moment the mouse hovers over the button

                if button.collidepoint(mouse_pos):
                    # pritns current location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))


    pygame.draw.rect(screen, [255, 0, 0], button) # draw objects down here

    #update 
    all_sprites.update()

    #draw / render
    screen.fill(BLACK)
    screen.blit(BackGround.image, BackGround.rect)
    all_sprites.draw(screen)
    #After drawing everything, flip the display.
    pygame.display.flip()

pygame.quit()