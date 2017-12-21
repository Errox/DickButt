#This script is for playing and moving around a sprite
#import all lib's
 
 
def start_astrodoge():
    import pygame
    import random
    import os
    import menu
    import highscore
 
    #define pygame core
    WIDTH   = 900
    HEIGHT  = 900
    FPS     = 30
    X       = 500
    Y       = 100
    MOB_AMOUNT = 100
 
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
 
    #setting up a player class
    class player(pygame.sprite.Sprite):
        #sprite and other properties for the player
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = pygame.image.load('resource/images/astrodoge/player/spaceship.png').convert()
            self.image.set_colorkey(BLACK)
            self.rect   = self.image.get_rect()
            self.radius = 23
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 0
 
        #This function is given to update the player itself into the game
        def update(self):
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -10
            if keystate[pygame.K_RIGHT]:
                self.speedx = 10
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
        
        #this is a function to add a bullet from the player itself. 
        def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
 
 
 
    #Setting up a mob ( in this case a astroid )
    class Mob(pygame.sprite.Sprite):
        #defining itself with properties
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('resource/images/astrodoge/mobs/Projectile_426.png').convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = int(self.rect.width * .8 / 2)
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
 
        #given instructions what to do on a update
        def update(self):
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
 
    #Setting up a bullet
    class Bullet(pygame.sprite.Sprite):
        #give properties to the bullet itself
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('resource/images/astrodoge/projectiles/Projectile_710.png').convert()
            # self.image = pygame.transform.scale(self.image, (150, 150))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = -10
        #function to define the functions inside a update
        def update(self):
            self.rect.y += self.speedy
            #kill if off top screen
            if self.rect.bottom < 0:
                self.kill()
            
 
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
    pygame.display.set_caption("Astrodoge")
     
    #set FTP rate of clock ticks. 
    clock = pygame.time.Clock()
 
 
 
    #Preload images for the background
    background = pygame.image.load('resource/images/astrodoge/backgrounds/background_2.png').convert()
    background_rect = background.get_rect()
 
    #loading all sprites 
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = player()
    all_sprites.add(player)
    
    #loading all mobs in
    for i in range(MOB_AMOUNT):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot() 
 
        #update 
        all_sprites.update()
         
        #collision for bullet against mobs
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
 
        #collision if player hit mobs
        hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
        if hits:
            menu.start_menu()
            running = False
            
        #draw / render
        screen.fill(BLACK)
        screen.blit(background, background_rect)
 
        all_sprites.draw(screen)
        #After drawing everything, flip the display.
        pygame.display.flip()
 
    pygame.quit()