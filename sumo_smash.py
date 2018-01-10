def start_sumo_smash():
    import pygame
    import random
    import menu
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

    font = pygame.font.SysFont('Arcadepix.ttf', 30) 
    level = 1

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
            self.right = 850
            self.left = 50
            self.top = 50
            self.bottom = 850 
            self.heart_amount = 3
            self.is_hit = False

        def update(self):
            keystate = pygame.key.get_pressed()
            #self.speedy = 0
            #self.speedx = 0
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
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((60, 60))
            self.image.fill(BLUE)
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
            self.image.fill(BLUE)
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
            self.image.fill(BLUE)
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
    background = pygame.image.load('resource/images/sumo_smash/platformlevel1.png').convert()
    background_rect = background.get_rect()

    # Game loop
    running = True
    while running:
        time = time - 1
        level = 2
        if time == 9700: 
            background = pygame.image.load('resource/images/sumo_smash/platformlevel2.png').convert()
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
            background = pygame.image.load('resource/images/sumo_smash/platformlevel3.png').convert() 
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
            background = pygame.image.load("resource/images/sumo_smash/platformlevel1.png").convert() 
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
            player.right = 850
            player.left = 50
            player.top = 50
            player.bottom = 850 
        
        print (time)
        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
        
        count += 10
        score = int(count)

        # Update
        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            game_over.start(score, 3)
            running = False
        if player.alive == False:
            running = False
            game_over.start(score, 3)

        levels = "level 1"
        
        screen.fill(backround)
        screen.blit(background, background_rect)
        pygame.draw.rect(screen, BLACK, [block_1, 0, 500, 900]) # left
        pygame.draw.rect(screen, BLACK, [block_2, 0, 500, 900]) # Richt
        pygame.draw.rect(screen, BLACK, [0, block_3, 900, 500]) # bottom
        pygame.draw.rect(screen, BLACK, [0, block_4, 900, 500]) # top
        #pygame.draw.ellipse(screen, RED, (75, 75, 750, 750), 10)
        all_sprites.draw(screen)
        scoretext = font.render("Score {0}".format(score), 1, WHITE)
        screen.blit(scoretext, (5, 10))
        objectivetext = font.render(levels , 1, BLUE)
        screen.blit(objectivetext, (595, 10))
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
            game_over.start(score)

             
        # *after* drawing everything, flip the display
        pygame.display.flip()

        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            if not player.is_hit:
                player.heart_amount -= 1
                player.is_hit = True
        else:
            player.is_hit = False

    pygame.quit()
    quit()

