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
MOB_AMOUNT = 100
sound = pygame.mixer.init()

#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
size = [200, 200]
bg = [255, 255, 255]


#geluid bij bullit
pygame.mixer.init


#setting up a player class
class player(pygame.sprite.Sprite):
    #sprite and other properties for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load('images/spaceship/Ship_big_blue.png').convert()
        self.image = pygame.transform.scale(self.image, (90, 70))
        self.image.set_colorkey(BLACK)
        self.rect   = self.image.get_rect()
        self.radius = 23
        self.rect.centerx = WIDTH / 6
        self.rect.bottom = HEIGHT - 60
        self.speedx = 0
        self.speedy = 0

    #This function is given to update the player in the game
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        if keystate[pygame.K_UP]:
            self.speedy = -10
        if keystate[pygame.K_DOWN]:
            self.speedy = 10
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > HEIGHT:
            self.rect.top = 0
    
    #This is a function to shoot a bullet from the player itself. 
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


#Setting up a bullet
class Bullet(pygame.sprite.Sprite):
    #give properties to the bullet itself
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/projectiles/bullet.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    #function to define the functions inside an update
    def update(self):
        self.rect.y += self.speedy

        #kill if off top screen
        if self.rect.bottom < 0:
            self.kill()



#set x and y of the window on screen. (EXPIRIMENTAL)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)


#Start Pygame
pygame.init() 


#Defineeer de groote en breedte van de gme
screen = pygame.display.set_mode((WIDTH, HEIGHT))


#Verrander titel
pygame.display.set_caption("SPLACEHOLDER")


#Setup voor de fps 
clock = pygame.time.Clock()


#render de images voor de background

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = player()
all_sprites.add(player)

bullet_sound = pygame.mixer.Sound('sounds/pewpew/sfx_wpn_laser10.wav')
#de main game loops
running = True
while running:
    # Laat de clock ticken op de fps
    clock.tick(FPS)

    #kijk of er een event is 
    for event in pygame.event.get():
        #Check of de exit knop is ingedrukt
        if event.type == pygame.QUIT:
            running = False
        #als spatsie word ingedrukt moet er een kogel afgeschoten worden
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                bullet_sound.play()
                player.shoot()

                # pygame.mixer.Sound.play()
    #updaten van alle sprites
    all_sprites.update()
    screen.fill(WHITE)
    # screen.blit(background, background_rect)

    all_sprites.draw(screen)
    pygame.display.flip()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()