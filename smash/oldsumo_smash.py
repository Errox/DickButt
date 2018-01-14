def start_sumo_smash():
    import pygame
    import random
    import menu
    import soundboard
    import game_over

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

    time = 10_000
    count = 0 

    font = pygame.font.Font('resource/fonts/Arcadepix.ttf', 30)
    level = 1

    walk_1 = pygame.image.load('smash/walk_1.png')
    walk_2 = pygame.image.load('smash/walk_2.png')
    walk_3 = pygame.image.load('smash/walk_3.png')
    walk_4 = pygame.image.load('smash/walk_4.png')
    walk_5 = pygame.image.load('smash/walk_5.png')
    walk_6 = pygame.image.load('smash/walk_6.png')
    walk_7 = pygame.image.load('smash/walk_7.png')
    walk_8 = pygame.image.load('smash/walk_8.png')

    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("INVATION OF THE UNKNOWN")
    clock = pygame.time.Clock()
    soundboard.ast_main()
    start_init = True
    pause = False

    #Quit_Butt = pygame.image.load('resource/images/select_planet/button_quit_small.png')
    #screen.blit(Quit_Butt, [5, 5])


    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = walk_1
            self.image.set_colorkey(WHITE)                             
            self.image = pygame.transform.scale(self.image, (40, 40))  
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.centery = HEIGHT / 2
            self.speedx = 0
            self.speedy = 0
            self.current_frame = 0
            self.last_update = 0
            self.alive = True
            self.right = 850
            self.left = 50
            self.top = 50
            self.bottom = 850 
            self.heart_amount = 3
            self.is_hit = False
            self.direction = 0
            self.timer = 0

        def update(self):
            self.timer += 1
            if self.timer <= 3:
                self.image = walk_1
                self.image = pygame.transform.rotate(self.image, self.direction)
            elif self.timer <= 6:
                self.image = walk_2
                self.image = pygame.transform.rotate(self.image, self.direction)
            elif self.timer <= 9:
                self.image = walk_3  
                self.image = pygame.transform.rotate(self.image, self.direction)
            elif self.timer <= 12:
                self.image = walk_4 
                self.image = pygame.transform.rotate(self.image, self.direction)
            elif self.timer <= 15:
                self.image = walk_5
                self.image = pygame.transform.rotate(self.image, self.direction)
            elif self.timer <= 18:
                self.image = walk_6
                self.image = pygame.transform.rotate(self.image, self.direction)
            elif self.timer <= 21:
                self.image = walk_7
                self.image = pygame.transform.rotate(self.image, self.direction)
            elif self.timer <= 24:
                self.image = walk_8
                self.image = pygame.transform.rotate(self.image, self.direction)
            else:
                self.timer = 0

            keystate = pygame.key.get_pressed()
            #self.speedy = 0
            #self.speedx = 0
            if keystate[pygame.K_LEFT]:
                self.direction = 270
                self.speedx = -10
                self.speedy = 0
            if keystate[pygame.K_RIGHT]:
                self.direction = 90         
                self.speedx = 10
                self.speedy = 0
            if keystate[pygame.K_UP]:
                self.direction = 180
                self.speedy = -10
                self.speedx = 0
            if keystate[pygame.K_DOWN]: 
                self.direction = 360
                self.speedy = 10
                self.speedx = 0  
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if  self.rect.right > self.right:
                self.rect.right = 850
                self.alive = False
            if self.rect.left < self.left:
                self.rect.left = 50
                self.alive = False
            if self.rect.top < self.top:
                self.rect.top = 50
                self.alive = False
            if self.rect.bottom > self.bottom:
                self.rect.bottom = 850
                self.alive = False



    class Mob1(pygame.sprite.Sprite):
        def __init__(self):
            #goed
            pygame.sprite.Sprite.__init__(self)
            self.image  = pygame.image.load('resource/images/sumo_smash/alien_2.png')
            self.image = pygame.transform.scale(self.image, (60, 60))
            self.image = pygame.transform.rotate(self.image, 270)
            self.image.set_colorkey(BLACK)   
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
            #top to bottom
            pygame.sprite.Sprite.__init__(self)
            self.image  = pygame.image.load('resource/images/sumo_smash/alien_2.png')
            self.image = pygame.transform.scale(self.image, (60, 60))
            self.image = pygame.transform.rotate(self.image, 180)
            self.image.set_colorkey(BLACK)  
            #self.image.set_colorkey(WHITE)  
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
            self.image  = pygame.image.load('resource/images/sumo_smash/alien_2.png')
            self.image = pygame.transform.scale(self.image, (60, 60))
            self.image = pygame.transform.rotate(self.image, 90)
            self.image.set_colorkey(BLACK)   
            #self.image.fill(BLUE)
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
            self.image  = pygame.image.load('resource/images/sumo_smash/alien_2.png')
            self.image = pygame.transform.scale(self.image, (60, 60))
            self.image.set_colorkey(BLACK)              
            #self.image = pygame.Surface((60, 60))
            #self.image.fill(BLUE)
            self.rect = self.image.get_rect()
            self.rect.x = 450
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
    walls = pygame.sprite.Group()
    all_sprites.add(player)
    for i in range(1):
        m1 = Mob1()
        m2 = Mob2()
        m3 = Mob3()
        m4 = Mob4()
        all_sprites.add(m1, m2, m3, m4)
        mobs.add(m1, m2, m3, m4)
    if time == 9800:
        for i in range(2):
            m1 = Mob1()
            m2 = Mob2()
            m3 = Mob3()
            m4 = Mob4()
            all_sprites.add(m1, m2, m3, m4)
            mobs.add(m1, m2, m3, m4)

    #blocks = good
    block_1 = -450
    block_2 = 850
    block_3 = 850
    block_4 = -450

    backround = YELLOW
    background = pygame.image.load('resource/images/sumo_smash/grass_14.png').convert()
    background = pygame.transform.scale(background, (900, 900))
    background_rect = background.get_rect()
    Quit_Butt = pygame.image.load('resource/images/select_planet/button_quit_small.png')
    screen.blit(Quit_Butt, [5, 5])

    stars_1 = pygame.transform.scale(pygame.image.load('resource/images/sumo_smash/stars_bg.png'),(500, 900))
    stars_2 = pygame.transform.scale(pygame.image.load('resource/images/sumo_smash/stars_bg.png'),(500, 900))
    stars_3 = pygame.transform.scale(pygame.image.load('resource/images/sumo_smash/stars_bg.png'),(900, 500))
    stars_4 = pygame.transform.scale(pygame.image.load('resource/images/sumo_smash/stars_bg.png'),(900, 500))

    # Game loop
    running = True
    while running:
        
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
                print (event)
                #Check of de exit knop is ingedrukt
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
                #als esc ingedrukt wordt pauseert het spel
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = True
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
                            start_Sumo_smash()
                            print('goes to cheet sheet.')
            #flip the display.
            pygame.display.flip()
        
        while pause == False:                  
            time = time - 1
            level = 2
            if time == 9700:
                block_1 = -400
                block_2 = 800
                block_3 = 800
                block_4 = -400
                for i in range(1):
                    m1 = Mob1()
                    m2 = Mob2()
                    m3 = Mob3()
                    m4 = Mob4()
                    all_sprites.add(m1, m2, m3, m4)
                    mobs.add(m1, m2, m3, m4)
                player.right = 800
                player.left = 100
                player.top = 100
                player.bottom = 800 
            level = 3    
            if time == 9300:
                block_1 = -350
                block_2 = 750
                block_3 = 750
                block_4 = -350
                for i in range(0):
                    m1 = Mob1()
                    m2 = Mob2()
                    m3 = Mob3()
                    m4 = Mob4()
                    all_sprites.add(m1, m2, m3, m4)
                    mobs.add(m1, m2, m3, m4)
                player.right = 750
                player.left = 150
                player.top = 150
                player.bottom = 750 
            level = 4   
            if time == 9000:
                block_1 = -450
                block_2 = 850
                block_3 = 850
                block_4 = -450
                for i in range(1):
                    m1 = Mob1()
                    m2 = Mob2()
                    m3 = Mob3()
                    m4 = Mob4()
                    all_sprites.add(m1, m2, m3, m4)
                    mobs.add(m1, m2, m3, m4)
            level = 5
            if time == 8700:
                block_1 = -400
                block_2 = 800
                block_3 = 800
                block_4 = -400
                for i in range(0):
                    m1 = Mob1()
                    m2 = Mob2()
                    m3 = Mob3()
                    m4 = Mob4()
                    all_sprites.add(m1, m2, m3, m4)
                    mobs.add(m1, m2, m3, m4)
                player.right = 800
                player.left = 100
                player.top = 100
                player.bottom = 800      
               

                
            print (time)
            # keep loop running at the right speed
            clock.tick(FPS)
            # Process input (events)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = True

                        soundboard.pause()
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 5 and pygame.mouse.get_pos()[1] >= 5:
                        if pygame.mouse.get_pos()[0] <= 155 and pygame.mouse.get_pos()[1] <= 53:
                            menu.start_menu()
            count += 5
            score = int(count)

            # Update
            all_sprites.update()

            hits = pygame.sprite.spritecollide(player, mobs, False)
            
            if player.alive == False:
                running = False
                game_over.start(score, 4)

                
            screen.fill(backround)
            screen.blit(background, background_rect)
            screen.blit(stars_1, [block_1, 0])
            screen.blit(stars_2, [block_2, 0])
            screen.blit(stars_3, [0, block_3])
            screen.blit(stars_4, [0, block_4])

            #pygame.draw.rect(screen, BLACK, [block_1, 0, 500, 900]) # left
            #pygame.draw.rect(screen, BLACK, [block_2, 0, 500, 900]) # Richt
            #pygame.draw.rect(screen, BLACK, [0, block_3, 900, 500]) # bottom
            #pygame.draw.rect(screen, BLACK, [0, block_4, 900, 500]) # top
            #pygame.draw.ellipse(screen, RED, (75, 75, 750, 750), 10)

            all_sprites.draw(screen)
            quit_button         = pygame.transform.scale(pygame.image.load ('resource/images/select_planet/button_quit_small.png'), (42,40))
            quit_rect           = quit_button.get_rect()
            screen.blit(quit_button, (5,5))    

            scoretext = font.render("Score {0}".format(score), 1, WHITE)
            screen.blit(scoretext, (750, 10))
            if player.heart_amount == 3:
                hearts = pygame.transform.scale(pygame.image.load ('resource/UI/spacestrike/heart_3.png'), (130,45))
                screen.blit(hearts, [350, 0])
            if player.heart_amount == 2:
                hearts = pygame.transform.scale(pygame.image.load ('resource/UI/spacestrike/heart_2.png'), (130,45))
                screen.blit(hearts, [350, 0])
            if player.heart_amount == 1:
                hearts = pygame.transform.scale(pygame.image.load ('resource/UI/spacestrike/heart_1.png'), (130,45))
                screen.blit(hearts, [350, 0])
            if player.heart_amount == 0:
                player.alive = False
                print('game over')
                game_over.start(score, 4)


                
            # *after* drawing everything, flip the display
            pygame.display.flip()

            hits = pygame.sprite.spritecollide(player, mobs, False)
            if hits:
                if not player.is_hit:
                    player.heart_amount -= 1
                    player.is_hit = True
                    soundboard.bullet_on_hit_friendly()
            else:
                player.is_hit = False

    pygame.quit()
    quit()