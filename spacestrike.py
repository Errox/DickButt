#This script is for playing and moving around a sprite
#import all lib's + intergratie

def start_spacestrike():
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
    sound = pygame.mixer.init()
    MOB_AMOUNT = 40

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
            self.image  = pygame.image.load('resource/images/splaceholder/spaceship/Ship_big_blue.png').convert()
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
            self.speedy = 0
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
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
            if self.rect.top < 0:
                self.rect.top = 0

        #This is a function to shoot a bullet from the player itself. 
        def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

    #setting up a enemy class
    class enemy(pygame.sprite.Sprite):
        #sprite and other properties for the enemy
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = pygame.image.load('resource/images/splaceholder/enemy/enemy.png').convert()
            self.image = pygame.transform.scale(self.image, (90, 70))
            self.image.set_colorkey(BLACK)
            self.rect   = self.image.get_rect()
            self.radius = 23
            self.rect.x = 0
            self.rect.y = 0
            self.speedx = 0
            self.speedy = 0

        #This function is given to update the player in the game
        def update(self): 
            self.speedx = random.randrange(1, 10)
            self.speedy = random.randrange(1, 10)
            self.rect.x += self.speedx
            self.rect.y += self.speedy
        #kill if off screen
            if self.rect.bottom < 0:
                self.kill()

        #This is a function to shoot a bullet from enemy at random
        def shoot_AI(self):
            AI_Bullet = AI_Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(AI_Bullet)
            AI_Bullets.add(AI_Bullet)



    #Setting up a bullet
    class Bullet(pygame.sprite.Sprite):
        #give properties to the bullet itself
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('resource/images/splaceholder/projectiles/bullet.png').convert()
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

   #Setting up a AI_bullet
    class AI_Bullet(pygame.sprite.Sprite):
        #give properties to the bullet itself
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('resource/images/splaceholder/projectiles/bullet.png').convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = 10
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


    #Defineeer de groote en breedte van de game
    screen = pygame.display.set_mode((900, 900))


    #Verander titel
    pygame.display.set_caption("SPLACEHOLDER")


    #Setup voor de fps 
    clock = pygame.time.Clock()


    # images for the background
    surface = pygame.image.load('resource/images/splaceholder/background/background_splaceholder.png').convert()
    surface_rect = surface.get_rect()

    print (surface)
    print (surface_rect)

    #loading all sprites
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = player()
    all_sprites.add(player)
    enemys = pygame.sprite.Group()
    AI_bullets = pygame.sprite.Group()


    for i in range(MOB_AMOUNT):
        m = enemy()
        all_sprites.add(m)
        enemys.add(m)
        

    bullet_sound = pygame.mixer.Sound('resource/music/splaceholder/sounds/sfx_wpn_laser10.wav')
    #de main game loops
    running = True
    while running:
        # Laat de clock ticken op de fps
        clock.tick(FPS)

        #render background
        screen.fill(BLACK)
        screen.blit(surface, surface_rect)

        #kijk of er een event is 
        for event in pygame.event.get():
            print (event)
            #Check of de exit knop is ingedrukt
            if event.type == pygame.QUIT:
                running = False

            #chance_shooting = random.randrange(1,10)
            #if chance_shooting == 7:
                #enemys.shoot()

            #als spatie word ingedrukt moet er een kogel afgeschoten worden
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    bullet_sound.play()
                    player.shoot()

                    # pygame.mixer.Sound.play()
            
        
        
       #collision for bullet against enemy
        hits = pygame.sprite.groupcollide(enemys, bullets, True, True)
        for hit in hits:
            m = enemy()
            all_sprites.add(m)
            enemys.add(m)
 
        #collision if player hit enemy
        hits = pygame.sprite.spritecollide(player, enemys, False, pygame.sprite.collide_circle)
        if hits:
            menu.start_menu()
            running = False
                
    
        #updaten van alle sprites
        all_sprites.update()

        all_sprites.draw(screen)
        pygame.display.flip()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    pygame.quit()


# start_splaceholder()