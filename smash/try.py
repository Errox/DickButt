import pygame
import random

WIDTH = 900
HEIGHT = 900
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ALIEN INVATION")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        self.alive = True

    def update(self, top, bottom, left, right):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
                self.speedx = -10
                self.speedy = 0
        if keystate[pygame.K_RIGHT]:
                self.speedx = 10
                self.speedy = 0
        if keystate[pygame.K_UP]:
                self.speedy = -10
                self.speedx = 0
        if keystate[pygame.K_DOWN]:
                self.speedy = 10  
                self.speedx = 0     
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > right:
           self.rect.right = right
           self.alive = False
        if self.rect.left < left:
           self.rect.left = left
           self.alive = False
        if self.rect.top < top:
           self.rect.top = top
           self.alive = False
        if self.rect.bottom > bottom:
           self.rect.bottom = bottom 
           self.alive = False



class Mob1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-500, -400)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        self.speedx = random.randrange(10, 15)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > 950:
            self.rect.x = random.randrange(-100, -40)
            self.rect.y = random.randrange(HEIGHT - self.rect.height)
            self.speedx = random.randrange(10, 15)

class Mob2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-500, -400)
        self.speedy = random.randrange(10, 15)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 50:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(10, 15)

class Mob3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = random.randrange(50, 850)
        self.speedy = random.randrange(10, 15)

    def update(self):
        self.rect.x -= self.speedy
        if self.rect.left < -50:
            self.rect.x = 950
            self.rect.y = random.randrange(50, 850)
            self.speedx = random.randrange(10, 15)

class Mob4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 850)
        self.rect.y = 1200
        self.speedy = random.randrange(10, 15)

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.top < -50:
            self.rect.x = random.randrange(50, 850)
            self.rect.y = 1000
            self.speedy = random.randrange(10, 15)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
for i in range(1):
    m1 = Mob1()
    m2 = Mob2()
    m3 = Mob3()
    m4 = Mob4()
    all_sprites.add(m1, m2, m3, m4)
    mobs.add(m1, m2, m3, m4)

time = 10_000

block_1 = -450
block_2 = 850
block_3 = 850
block_4 = -450

# Game loop
running = True
while running:
    time = time - 1
    print (time)
    if time == 9900: 
        block_1 = -350
        block_2 = 750
        block_3 = 750
        block_4 = -350

    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        

    # Update
    all_sprites.update()
    player.update(block_4, block_3, block_1, block_2)

    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
    if player.alive == False:
        running = False


    # Draw / render
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [block_1, 0, 500, 900]) # left
    pygame.draw.rect(screen, RED, [block_2, 0, 500, 900]) # Richt
    pygame.draw.rect(screen, RED, [0, block_3, 900, 500]) # bottom
    pygame.draw.rect(screen, RED, [0, block_4, 900, 500]) # top
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()