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

    def update(self):
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
        if self.rect.right > 850:
           self.rect.right = 850 
        if self.rect.left < 50:
           self.rect.left = 50
        if self.rect.top < 50:
           self.rect.top = 50
        if self.rect.bottom > 850:
           self.rect.bottom = 850   


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
        self.rect.x = 950
        self.rect.y = 300
        self.speedy = 15

    def update(self):
        self.rect.x -= self.speedy
        if self.rect.left < -50:
            self.rect.x = 950
            self.rect.y = 300
            self.speedx = 15

class Mob4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1, 850)
        self.rect.y = random.randrange(900, 1000)
        self.speedy = random.randrange(10, 15)

    def update(self):
        self.rect.y -= self.speedy
    if self.rect.top < 50:
        self.rect.x = random.randrange(1, 850)
        self.rect.y = random.randrange(900, 1000)
        self.speedy = random.randrange(10, 15)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
walls = pygame.sprite.Group()
all_sprites.add(player)
for i in range(1):
    m1 = Mob1()
    m2 = Mob2()
    m3 = Mob3()
    m4 = Mob4()
    all_sprites.add(m1, m2, m3, m4)
    mobs.add(m1, m2, m3, m4)


# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        

    # Update
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False



    # Draw / render
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [-450, 0, 500, 900]) # left
    pygame.draw.rect(screen, RED, [850, 0, 500, 900]) # Richt
    pygame.draw.rect(screen, RED, [0, 850, 900, 500]) # bottom
    pygame.draw.rect(screen, RED, [0, -450, 900, 500]) # top
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()