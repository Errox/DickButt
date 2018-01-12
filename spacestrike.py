#import all libraries + intergratie
heart_amount = 3
def start_spacestrike():
    import pygame
    import time
    import random
    import os
    import menu
    import highscore
    import game_over
    import soundboard

    #define core
    WIDTH   = 900
    HEIGHT  = 900
    FPS     = 30
    X       = 500
    Y       = 100
    enemy_amount = random.randrange(7,17)
    global heart_amount
    heart_amount = 3
    start_init = True
    score   = 0
    global planet_hp
    planet_hp = 9001
    pause = False
    startTime = time.time()
    count = 5

    #define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    size = [200, 200]
    bg = [255, 255, 255]

    #set up assets
    game_folder = os.path.dirname(__file__)
    img_folder  = os.path.join(game_folder, "img")


    #player class
    class player(pygame.sprite.Sprite):
        #sprite and properties
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = pygame.image.load('resource/images/spacestrike/spaceship/Ship_big_purple.png')
            self.image = pygame.transform.scale(self.image, (70, 55))
            self.image.set_colorkey(BLACK)
            self.rect   = self.image.get_rect()
            self.radius = 15
            self.rect.centerx = WIDTH / 6
            self.rect.bottom = HEIGHT - 60
            self.speedx = 0
            self.speedy = 0

        #update function in-game
        def update(self):
            self.image  = pygame.image.load('resource/images/spacestrike/spaceship/Ship_big_purple.png')
            self.image = pygame.transform.scale(self.image, (134, 75))
            self.image.set_colorkey(BLACK)
            self.speedx = 0
            self.speedy = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.image  = pygame.image.load('resource/images/spacestrike/spaceship/Ship_big_purple_booster.png')
                self.image = pygame.transform.scale(self.image, (134, 75))
                self.image.set_colorkey(BLACK)
                self.speedx = -10
            if keystate[pygame.K_RIGHT]:
                self.image  = pygame.image.load('resource/images/spacestrike/spaceship/Ship_big_purple_booster.png')
                self.image = pygame.transform.scale(self.image, (134, 75))
                self.image.set_colorkey(BLACK)
                self.speedx = 10
            if keystate[pygame.K_UP]:
                self.image  = pygame.image.load('resource/images/spacestrike/spaceship/Ship_big_purple_booster.png')
                self.image = pygame.transform.scale(self.image, (134, 75))
                self.image.set_colorkey(BLACK)
                self.speedy = -10
            if keystate[pygame.K_DOWN]:
                self.image  = pygame.image.load('resource/images/spacestrike/spaceship/Ship_big_purple_booster.png')
                self.image = pygame.transform.scale(self.image, (134, 75))
                self.image.set_colorkey(BLACK)
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

        #function to shoot friendly bullet 
        def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

    #enemy class
    class enemy(pygame.sprite.Sprite):
        #sprite and properties for enemy
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = pygame.image.load('resource/images/spacestrike/enemy/enemy.png').convert()
            self.image = pygame.transform.scale(self.image, (70, 50))
            self.image.set_colorkey(BLACK)
            self.rect   = self.image.get_rect()
            self.radius = 23
            self.rect.x = random.randrange(0,830)
            self.rect.y = 0
            self.speedx = random.randrange(3,7)
            self.speedy = random.randrange(3,7)
            self.speedrand = random.choice([True, False])

        #update player
        def update(self): 
            self.rect.y += self.speedy
            if self.speedrand == True:
                self.rect.x += self.speedx
            else:
                self.rect.x += self.speedx * -1
        #kill if off the screen
            if self.rect.y > 810:
                self.kill()
                global planet_hp
                planet_hp -= 125
                m = enemy()
                all_sprites.add(m)
                enemys.add(m)     
            if self.rect.x > 830:
                self.speedx = self.speedx * -1
            if self.rect.x < 0:
                self.speedx = self.speedx * -1
            if random.randrange(1,100) < 2:
                enemy.shoot_AI(self,self.rect.centerx,self.rect.bottom)

        #function for random enemy shooting
        def shoot_AI(self,x,y):
            en_bullet = AI_Bullet(x,y)
            all_sprites.add(en_bullet)
            en_bullet.add()

    #friendly bullet
    class Bullet(pygame.sprite.Sprite):
        #image and properties for bullet
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('resource/images/spacestrike/projectiles/bullet.png').convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = -10
        #function to define the functions inside update
        def update(self):
            self.rect.y += self.speedy

            #kill if off the top screen
            if self.rect.bottom < 0:
                self.kill()

   #AI_bullet
    class AI_Bullet(pygame.sprite.Sprite):
        #properties and image for AI bullet
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('resource/images/spacestrike/projectiles/en_bullet.png').convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = 10
     
        #function to define the functions inside an update
        def update(self):
            self.rect.y += self.speedy
            if self.rect.colliderect(player.rect):
                soundboard.bullet_on_hit_friendly()
                self.kill()
                lose_heart()

            #kill if off top screen
            if self.rect.y > 900:
                self.kill()

    #start Pygame
    pygame.init() 

    #initiate library sonuds
    soundboard.spst_main()

    #set size of screen
    screen = pygame.display.set_mode((900, 900))

    #change title in window
    pygame.display.set_caption("SPACESTRIKE")

    #set up fps
    clock = pygame.time.Clock()

    #images for the background
    surface = pygame.image.load('resource/images/spacestrike/background/background_base.png').convert()
    surface_rect = surface.get_rect()

    print (surface)
    print (surface_rect)

    #load in font and sprites
    font = pygame.font.Font('resource/fonts/Arcadepix.ttf', 30)
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = player()
    all_sprites.add(player)
    enemys = pygame.sprite.Group()
    en_bullets = pygame.sprite.Group()

    # add mobs
    for i in range(enemy_amount):
        m = enemy()
        all_sprites.add(m)
        enemys.add(m)

    startTime = time.time() 
    count = 5 
    #main game loop
    running = True
    while running:
        while pause == True:
            clock.tick(FPS)
            mm_button        = pygame.image.load('resource/images/pause_screen/button_mm.png').convert()
            resume_button    = pygame.image.load('resource/images/pause_screen/button_resume.png').convert()
            restart_button   = pygame.image.load('resource/images/pause_screen/button_restart.png').convert()
            mm_rect          = mm_button.get_rect()
            resume_rect      = resume_button.get_rect()
            restart_rect     = restart_button.get_rect()
            screen.blit(mm_button, (325,550))
            screen.blit(resume_button, (325,470))
            screen.blit(restart_button, (325,390))

            for event in pygame.event.get():
                print (event)
                
                #press esc for pause
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = False
                        soundboard.resume()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 325 and pygame.mouse.get_pos()[1] >= 550:
                        if pygame.mouse.get_pos()[0] <= 593 and pygame.mouse.get_pos()[1] <= 615:
                            menu.start_menu()
                    if pygame.mouse.get_pos()[0] >= 325 and pygame.mouse.get_pos()[1] >= 470:
                        if pygame.mouse.get_pos()[0] <= 593 and pygame.mouse.get_pos()[1] <= 535:
                            pause = False
                            soundboard.resume()
                    if pygame.mouse.get_pos()[0] >= 325 and pygame.mouse.get_pos()[1] >= 390:
                        if pygame.mouse.get_pos()[0] <= 593 and pygame.mouse.get_pos()[1] <= 455:
                            print('goes to cheet sheet.')
            #flip display.
            pygame.display.flip()

        while pause == False:
            
            time_alive = time.time() - startTime
            print (time_alive)
            
            #enemy increase
            if time_alive == count:
                count += 5
                m = enemy()
                all_sprites.add(m)
                enemys.add(m)
    
            #run loop at correct fps
            clock.tick(FPS)

            #check for events
            for event in pygame.event.get():
                #catch mouse pos if pressed on button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 5 and pygame.mouse.get_pos()[1] >= 5:
                        if pygame.mouse.get_pos()[0] <= 155 and pygame.mouse.get_pos()[1] <= 53:
                           menu.start_menu()
                 #check and close window
                if event.type == pygame.QUIT:
                    #closing window
                    running = False
                    pygame.quit()
                    quit()

                #shoot bullet with spacebar
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        soundboard.bullet_shoot_friendly()
                        player.shoot()
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                        soundboard.pause()
            
            #update
            all_sprites.update()

            #collision friendly bullet against enemy
            hits = pygame.sprite.groupcollide(enemys, bullets, True, True)
            if hits:
                score += 100
                soundboard.bullet_on_hit_enemy()
            for hit in hits:
                m = enemy()
                all_sprites.add(m)
                enemys.add(m)

            #collision player with enemy
            hits = pygame.sprite.spritecollide(player, enemys, True, pygame.sprite.collide_circle)
            if hits:
                soundboard.bullet_on_hit_friendly()
                lose_heart()

            #collision AI bullet with player
            hits = pygame.sprite.spritecollide(player, en_bullets, True, pygame.sprite.collide_circle)
            if hits:
                soundboard.bullet_on_hit_friendly()
                lose_heart()
            
            #function for hearts
            def lose_heart():
                global heart_amount
                heart_amount -= 1

            #draw/render and quit button
            if start_init == True:
                screen.fill(BLACK)
                start_init = False
            screen.blit(surface, surface_rect)
            
            quit_button         = pygame.transform.scale(pygame.image.load ('resource/images/select_planet/button_quit_small.png'), (42,40))
            quit_rect           = quit_button.get_rect()
            screen.blit(quit_button, (5,5))    
         
            
            #check lives, else load game_over screen
            if heart_amount == 3:
                hearts = pygame.transform.scale(pygame.image.load ('resource/UI/spacestrike/heart_3.png'), (130,45))
                screen.blit(hearts, [365, 0])
            elif heart_amount == 2:
                hearts = pygame.transform.scale(pygame.image.load ('resource/UI/spacestrike/heart_2.png'), (130,45))
                screen.blit(hearts, [365, 0])
            elif heart_amount == 1:
                hearts = pygame.transform.scale(pygame.image.load ('resource/UI/spacestrike/heart_1.png'), (130,45))
                screen.blit(hearts, [365, 0])
            else:
                print('game over')
                game_over.start(score, 2)
            if planet_hp <= 0:
                print('game over')                
                game_over.start(score, 2)

            #add score
            scoretext = font.render("Score  :  {0}".format(score), 1, WHITE)
            screen.blit(scoretext, (720, 5))

            planethealth = font.render("Veilea :  {0}".format(planet_hp), 1, WHITE)
            screen.blit(planethealth, (720, 25))
            
            #draw
            all_sprites.draw(screen)

            #flip display.
            pygame.display.flip()

    pygame.quit()