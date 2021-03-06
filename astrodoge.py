#This script is for playing and moving around a sprite
#import all lib's
heart_amount = 3
#start astrodoge
def start_astrodoge():
    import pygame
    import random
    import os
    import menu
    import time
    import cheat_sheet
    import highscore
    import cheat_sheet
    import game_over
    import cheat_sheet
    import soundboard
 
    #define pygame core
    WIDTH   = 900
    HEIGHT  = 900
    FPS     = 30
    level_gun = 1
    pause   = False
    seconds = 5
    delay_gun   = 500
    X       = 500
    spawnertje = 2
    Y       = 100
    MOB_AMOUNT = 10
    global heart_amount
    heart_amount = 3
    spawn_rate = 95
    startTime = time.time()
    start_init = True
    score   = 0
    health  = 9001
 
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

    #load all explosion animations
    explosion_anim = []
    for i in range(17):
        filename = 'resource/images/astrodoge/explosions/ship_expl_{}.png'.format(i)
        img = pygame.image.load(filename)
        img.set_colorkey(BLACK)
        img = pygame.transform.scale(img, (75, 75))
        explosion_anim.append(img)

    #setting up a player class
    class player(pygame.sprite.Sprite):
        #sprite and other properties for the player
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image  = pygame.image.load('resource/images/astrodoge/player/Ship_big_purple.png')                            
            self.image = pygame.transform.scale(self.image, (90, 70))
            self.image.set_colorkey(BLACK)
            self.rect   = self.image.get_rect()
            self.shoot_delay = delay_gun
            self.last_shot = pygame.time.get_ticks()
            self.radius = 23
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 30
            self.speedx = 0

        #This function is given to update the player itself into the game
        def update(self):
            self.speedx = 0
            self.image  = pygame.image.load('resource/images/astrodoge/player/Ship_big_purple.png') 
            self.image = pygame.transform.scale(self.image, (90, 70))
            self.image.set_colorkey(BLACK)
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.image  = pygame.image.load('resource/images/spacestrike/spaceship/Ship_big_purple_booster.png')
                self.image = pygame.transform.scale(self.image, (90, 70))
                self.image.set_colorkey(BLACK)
                self.speedx = -10
            if keystate[pygame.K_RIGHT]:
                self.image  = pygame.image.load('resource/images/spacestrike/spaceship/Ship_big_purple_booster.png')
                self.image = pygame.transform.scale(self.image, (90, 70))
                self.image.set_colorkey(BLACK)
                self.speedx = 10
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            if keystate[pygame.K_SPACE]:
                self.shoot()

        #setup a function to shoot
        def shoot(self):
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                soundboard.bullet_shoot_friendly()
                self.shoot_delay = delay_gun
                self.last_shot = now
                if level_gun >= 4 and level_gun <= 5:
                    bullet_l = Bullet(self.rect.left, self.rect.top)
                    all_sprites.add(bullet_l)
                    bullets.add(bullet_l)
                    bullet_r = Bullet(self.rect.right, self.rect.top)
                    all_sprites.add(bullet_r)
                    bullets.add(bullet_r)
                elif level_gun >= 6:
                    bullet_l = Bullet(self.rect.left, self.rect.top)
                    all_sprites.add(bullet_l)
                    bullets.add(bullet_l)
                    bullet_r = Bullet(self.rect.right, self.rect.top)
                    all_sprites.add(bullet_r)
                    bullets.add(bullet_r)
                    bullet = Bullet(self.rect.centerx, self.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                else:
                    bullet = Bullet(self.rect.centerx, self.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
            
 
    #Setting up a mob ( in this case a astroid )
    class Mob(pygame.sprite.Sprite):
        #defining itself with properties
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            randomizer = random.randrange(1,5)
            if randomizer == 1:
                self.image = pygame.image.load('resource/images/astrodoge/mobs/smol_rocks/blue_rock_1.png')
            elif randomizer == 2:
                self.image = pygame.image.load('resource/images/astrodoge/mobs/smol_rocks/ice_rock_1.png')
            elif randomizer == 3:
                self.image = pygame.image.load('resource/images/astrodoge/mobs/smol_rocks/lightblue_rock_1.png')
            elif randomizer == 4:
                self.image = pygame.image.load('resource/images/astrodoge/mobs/smol_rocks/rock_1.png')
            elif randomizer == 5: 
                self.image = pygame.image.load('resource/images/astrodoge/mobs/smol_rocks/vein_rock_1.png')
            
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = int(self.rect.width * .4 / 2)
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.health = random.randrange(1,3)
 
        #given instructions what to do on a update
        def update(self):
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
            # if self.rect.colliderect(bullets.rect):
            #     if health <= 0:
            #         self.kill()
            #     else:
            #         health -= 1
                
    class Mob_heavy(pygame.sprite.Sprite):
            #defining itself with properties
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            randomizer = random.randrange(1,5)
            if randomizer == 1:
                self.image = pygame.image.load('resource/images/astrodoge/mobs/big_rocks/blue_rock_big_1.png')
            elif randomizer == 2:
                self.image = pygame.image.load('resource/images/astrodoge/mobs/big_rocks/ice_rock_big_1.png')
            elif randomizer == 3:
                self.image = pygame.image.load('resource/images/astrodoge/mobs/big_rocks/lightblue_rock_big_1.png')
            elif randomizer == 4:
                self.image = pygame.image.load('resource/images/astrodoge/mobs/big_rocks/rock_big_1.png')
            elif randomizer == 5: 
                self.image = pygame.image.load('resource/images/astrodoge/mobs/big_rocks/vein_rock_big_1.png')
            
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
    
    class power_up(pygame.sprite.Sprite):
        #defining itself with properties
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('resource/images/astrodoge/powerups/power_up.png').convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = int(self.rect.width * .8 / 2)
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = (2)
 
        #given instructions what to do on a update
        def update(self):
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)

    class Explosion(pygame.sprite.Sprite):
        def __init__(self, center):
            pygame.sprite.Sprite.__init__(self)
            self.size = size
            self.image = explosion_anim[0]
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.frame = 0
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 50

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(explosion_anim):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = explosion_anim[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center

                
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
    soundboard.ast_main()
    # pygame.mixer.music.load("music/main_menu.ogg")
    # pygame.mixer.Sound.play(-1)
 
    #set height and width of the game
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
 
    #Set caption
    pygame.display.set_caption("Astrodoge")
     
    #set FTP rate of clock ticks. 
    clock = pygame.time.Clock()
  
    #Preload images for the background
    background = pygame.image.load('resource/images/astrodoge/backgrounds/basic_star_bg.png').convert()
    background_rect = background.get_rect()
    
    #loading in font
    font = pygame.font.Font('resource/fonts/Arcadepix.ttf', 30)
 
    #define all sprites
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = player()
    all_sprites.add(player)
    #time ticks
    newtime=pygame.time.get_ticks()
    oldtime=newtime
 
    for i in range(MOB_AMOUNT):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    time_now = time.time()
    #game loop
    running = True
    while running:
        #get a menu ready when pause is active
        while pause == True:
            clock.tick(FPS)
            mm_button        = pygame.image.load('resource/images/pause_screen/button_mm.png')
            resume_button    = pygame.image.load('resource/images/pause_screen/button_resume.png')
            restart_button   = pygame.image.load('resource/images/pause_screen/button_restart.png')
            mm_rect          = mm_button.get_rect()
            resume_rect      = resume_button.get_rect()
            restart_rect     = restart_button.get_rect()
            screen.blit(mm_button, (325,550))
            screen.blit(resume_button, (325,470))
            screen.blit(restart_button, (325,390))

            for event in pygame.event.get():
                #Check of de exit knop is ingedrukt
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
                #als esc ingedrukt wordt pauseert het spel
                elif event.type == pygame.KEYDOWN:
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
                            cheat_sheet.start(1)
            #flip the display.
            pygame.display.flip()
        #Play the game if pause isn't true
        while pause == False:
            time_alive = time.time() - startTime 
            if time_alive == seconds:
                seconds += random.randrange(1,7)
                spawn_rate = 30 
    
            if round(time_alive) == spawnertje:           
                power = power_up()
                all_sprites.add(power)
                powerups.add(power)
                spawnertje += random.randrange(15,30)

            
            spawn_random = random.randrange(1, 100) 

            if spawn_random > spawn_rate: 
                m = Mob() 
                all_sprites.add(m) 
                mobs.add(m) 

            # keep loop running at the right fps
            clock.tick(FPS)
    
            #process input (events)
            for event in pygame.event.get():
                 #Catch mouse position and if it's pressed on the button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 5 and pygame.mouse.get_pos()[1] >= 5:
                        if pygame.mouse.get_pos()[0] <= 155 and pygame.mouse.get_pos()[1] <= 53:
                           menu.start_menu()
                #check for closing the windows
                if event.type == pygame.QUIT:
                    #if the close button is pressed, the game will close
                    running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                        soundboard.pause()

            all_sprites.update()
        
            #collision for bullet against mobs
            hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
            if hits:
                score += 100
                soundboard.bullet_on_hit_enemy()
            for hit in hits:
                m = Mob()
                all_sprites.add(m)
                expl = Explosion(hit.rect.center)
                all_sprites.add(expl)
                mobs.add(m)

            hits = pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_circle)
            if hits:
                delay_gun -= 75
                level_gun += 1
                if level_gun == 4 and level_gun == 5:
                    delay_gun += 100
                soundboard.upgrade()

            #collision if player hit mobs
            hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
            if hits:
                soundboard.bullet_on_hit_friendly()
                expl = Explosion(hit.rect.center)
                all_sprites.add(expl)
                level_gun -= 1
                lose_heart()

            #draw / render
            if start_init == True:
                screen.fill(BLACK)
                start_init = False
            screen.blit(background, background_rect)

            quit_button         = pygame.transform.scale(pygame.image.load ('resource/images/select_planet/button_quit_small.png'), (42,40))
            quit_rect           = quit_button.get_rect()
            screen.blit(quit_button, (5,5))  

            def lose_heart():
                global heart_amount
                heart_amount -= 1
            
            #check how many lives the player has, else invoke the game_over scene 
            if heart_amount == 3:
                hearts = pygame.transform.scale(pygame.image.load ('resource/UI/spacestrike/heart_3.png'), (130,45))
                screen.blit(hearts, [365, 0])
            elif heart_amount == 2:
                hearts = pygame.transform.scale(pygame.image.load ('resource/UI/spacestrike/heart_2.png'), (130,45))
                screen.blit(hearts, [365, 0])
            elif heart_amount == 1:
                hearts = pygame.transform.scale(pygame.image.load ('resource/UI/spacestrike/heart_1.png'), (130,45))
                screen.blit(hearts, [365, 0])
            if heart_amount == 0:
                print('game over')
                game_over.start(score, 1)
                

            scoretext = font.render("Score :  {0}".format(score), 1, WHITE)
            screen.blit(scoretext, (720, 5))
            
            scoretext = font.render("Time    :  {0}".format(round(time_alive)), 1, WHITE) 
            screen.blit(scoretext, (720, 25)) 

            scoretext = font.render("Gun level :  {0}".format(level_gun), 1, WHITE) 
            screen.blit(scoretext, (720, 45)) 

            all_sprites.draw(screen)
            #After drawing everything, flip the display.
            pygame.display.flip()
    
    pygame.quit()