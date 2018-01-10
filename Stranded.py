
def start_Stranded():
    import pygame
    import menu
    import game_over
    import soundboard
    import pygame.locals
    import time

    # Global constants
    # images

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BEIGE = (255,211,155)
    BROWN = (139,121,94)
    GREY = (128, 128, 128)

    # score = 100000
    score = 10000

    startTime = time.time()
    # Screen size
    display_width = 900
    display_height = 900

    gameDisplay = pygame.display.set_mode((display_width,display_height))

    done = False

    # player controlled class
    class MG_Player(pygame.sprite.Sprite):

        # methods
        def __init__(self):
            # Constructor function

            # call the parent's constructor
            super().__init__()

            # create and color the blocks
            width = 50
            height = 75
            self.walking = False
            self.current_frame = 0
            self.last_update = 0
            self.load_images()
            self.image = pygame.image.load('resource/images/Character/Purple/Right/Stance/1.png').convert()
            self.image = pygame.transform.scale(self.image, (50, 75))
            #self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            # self.image = pygame.Surface([width, height])
            # self.image.fill(GREEN)


            # set speed of mg_player
            self.change_x = 0
            self.change_y = 0

            # list of sprites to walk against
            self.level = None
            # Inventory
            self.inventory = None
        def load_images(self):
            self.standing_frames = [pygame.image.load('resource/images/Stranded/player purple/s1.png').convert(),
                                    pygame.image.load('resource/images/Stranded/player purple/s2.png').convert()]
            for frame in self.standing_frames:
                frame.set_colorkey(BLACK)
            self.walk_frames_r = [pygame.image.load('resource/images/Stranded/player purple/1.png').convert(),
                                   pygame.image.load('resource/images/Stranded/player purple/2.png').convert(),
                                   pygame.image.load('resource/images/Stranded/player purple/3.png').convert(),
                                   pygame.image.load('resource/images/Stranded/player purple/4.png').convert(),
                                   pygame.image.load('resource/images/Stranded/player purple/5.png').convert(),
                                   pygame.image.load('resource/images/Stranded/player purple/6.png').convert(),
                                   pygame.image.load('resource/images/Stranded/player purple/7.png').convert(),
                                   pygame.image.load('resource/images/Stranded/player purple/8.png').convert(),
                                   pygame.image.load('resource/images/Stranded/player purple/9.png').convert()]
            self.walk_frames_l = []
            for frame in self.walk_frames_r:
                frame.set_colorkey(BLACK)
                self.walk_frames_l.append(pygame.transform.flip(frame, True, False))

        def update(self):
            # move the player
            self.animate()
            # calculate gravity
            self.calc_grav()

            # move left and right
            self.rect.x += self.change_x

            # check if an object has been hit
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:
                # if moving right
                # set right side to left if object is hit
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                elif self.change_x < 0:
                    # set left side to right side
                    self.rect.left = block.rect.right

            # move up and down
            self.rect.y += self.change_y

            # check if a monster has been hit
            monster_hit_list = pygame.sprite.spritecollide(self, self.level.monster_list, False)
            for block in monster_hit_list:
                nonlocal score
                score = 0
                global done
                done = True
                # if moving right
                # set right side to left if object is hit
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                elif self.change_x < 0:
                    # set left side to right side
                    self.rect.left = block.rect.right

            # move up and down 2
            self.rect.y += self.change_y

            # Check if MG_Player hits anything
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:

                # reset position based on objects
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom

                # set y speed to 0
                self.change_y = 0

            # Check if MG_Player hits monster
            monster_hit_list = pygame.sprite.spritecollide(self, self.level.monster_list, False)
            for block in monster_hit_list:

                score = 0
                done = True
                # reset position based on objects
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom

                # set y speed to 0
                self.change_y = 0

            # Check if MG_Player hits cship
            cship_hit_list = pygame.sprite.spritecollide(self, self.level.cship_list, False)
            for block in cship_hit_list:
                done = False
                if self.inventory:
                    done = True
                else:
                    done = False

            # Check if MG_Player hits strandedKey (Skey)
            skey_hit_list = pygame.sprite.spritecollide(self, self.level.skey_list, False)
            for block in skey_hit_list:
                done = False
                soundboard.st_collect()
                self.inventory = True
                block.hide()
        def animate(self):
            now = pygame.time.get_ticks()
            if self.change_x != 0:
                self.walking = True
            else:
                self.walking = False
            if self.walking:
                if now - self.last_update > 50:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.walk_frames_r)
                    bottom = self.rect.bottom
                    if self.change_x > 13:
                        self.image = self.walk_frames_r[self.current_frame]
                    else:
                        self.image = self.walk_frames_l[self.current_frame]


            if not self.walking:
                if now - self.last_update > 400:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                    bottom = self.rect.bottom
                    self.image = self.standing_frames[self.current_frame]
                    self.rect.bottom = bottom

        # calculating gravity
        def calc_grav(self):

            if self.change_y == 0:
                self.change_y = 10
            else:
                self.change_y += .50

            # check if ground bellow player
            if self.rect.y >= display_height - self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = display_height - self.rect.height

        def jump(self):
            # check if there is ground bellow so that the MG_Player can jump
            self.rect.y += 5
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y -= 5
            soundboard.st_jump()
            self.rect.y += 5
            monster_hit_list = pygame.sprite.spritecollide(self, self.level.monster_list, False)
            self.rect.y -= 5


            # if jump is possible change y speed
            if len(platform_hit_list) > 0 or self.rect.bottom >= display_height:
                self.change_y = -12

        # player movement speed
        def go_left(self):
            self.change_x = -14

        def go_right(self):
            self.change_x = 14

        def stop(self):
            self.change_x = 0


    class Monster(pygame.sprite.Sprite):
        # monster a sprite that kills

        def __init__(self, width, height):
            # monster constructor
            super().__init__()

            self.image = pygame.image.load('resource/images/Stranded/lava.png').convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            #self.image = pygame.Surface([width, height])
            #self.image.fill(RED)

            self.rect = self.image.get_rect()


    class Cship(pygame.sprite.Sprite):
        # Cship (crashed ship) the drop of point

        def __init__(self, width, height):
            # Cship constructor

            # call the parent's constructor
            super().__init__()
            self.image = pygame.image.load('resource/images/Stranded/cship.png')
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            # self.image.fill(BEIGE)

    class Skey(pygame.sprite.Sprite):
        # Skey (StrandedKey) the pick up point

        def __init__(self, width, height):
            # Skey constructor

            # call the parent's constructor
            super().__init__()

            self.image = pygame.image.load('resource/images/Stranded/Skey.png').convert()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            # Show by default
            self.hide_object = False

        def hide(self):
            # Block has been captured
            self.hide_object = True


    class Platform(pygame.sprite.Sprite):
        # platform layer can stand on

        def __init__(self, width, height):
            # platform constructor

            # call the parent's constructor
            super().__init__()

            self.image = pygame.Surface([width, height])
            self.image.fill(BROWN)

            self.rect = self.image.get_rect()


    class MovingMonster(Platform):
        # Creating a moving platform
        change_x = 0
        change_y = 0

        boundary_top = 0
        boundary_bottom = 0
        boundary_left = 0
        boundary_right = 0

        player = None

        level = None


        def update(self):
            # Move the platform
            self.image.fill(RED)

            # Move left/right
            self.rect.x += self.change_x

            # check if it hits the player
            hit = pygame.sprite.collide_rect(self, self.player)
            if hit:

                # if moving right, set right side to the left side of the object it's moving towards
                if self.change_x < 0:
                    self.player.rect.right = self.rect.left
                else:
                    # do the opposite of what to comment above states
                    self.player.rect.left = self.rect.right

            # Move up/down
            self.rect.y += self.change_y

            # check if the mg_player stands on the platform
            hit = pygame.sprite.collide_rect(self, self.player)
            if hit:
                # MG_player is hit, move the player.

                # reset position based on the top and/or bottom of the object
                if self.change_y < 0:
                    self.player.rect.bottom = self.rect.top
                else:
                    self.player.rect.top = self.rect.bottom

            # check if the platform must change directions
            if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
                self.change_y *= -1

            cur_pos = self.rect.x - self.level.world_shift
            if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
                self.change_x *= -1


    class MovingPlatform(Platform):
        # Creating a moving platform
        change_x = 0
        change_y = 0

        boundary_top = 0
        boundary_bottom = 0
        boundary_left = 0
        boundary_right = 0

        player = None

        level = None

        def update(self):
            # Move the platform
            self.image.fill(BLUE)

            # Move left/right
            self.rect.x += self.change_x

            # check if it hits the player
            hit = pygame.sprite.collide_rect(self, self.player)
            if hit:
                # if the player is hit, move the player

                # if moving right, set right side to the left side of the object it's moving towards
                if self.change_x < 0:
                    self.player.rect.right = self.rect.left
                else:
                    # do the opposite of what to comment above states
                    self.player.rect.left = self.rect.right

            # Move up/down
            self.rect.y += self.change_y

            # check if the mg_player stands on the platform
            hit = pygame.sprite.collide_rect(self, self.player)
            if hit:
                # MG_player is hit, move the player.

                # reset position based on the top and/or bottom of the object
                if self.change_y < 0:
                    self.player.rect.bottom = self.rect.top
                else:
                    self.player.rect.top = self.rect.bottom

            # check if the platform must change directions
            if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
                self.change_y *= -1

            cur_pos = self.rect.x - self.level.world_shift
            if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
                self.change_x *= -1


    class Level(object):
        # list of used sprites

        # camera moves with player
        world_shift = 0

        def __init__(self, mg_player):
            # constructor. pass in a handle to player
            self.platform_list = pygame.sprite.Group()
            self.monster_list = pygame.sprite.Group()
            self.cship_list = pygame.sprite.Group()
            self.skey_list = pygame.sprite.Group()
            self.MG_player = mg_player

            # Background image
            self.background = None

        # update everything in level
        def update(self):
            # update everything in level
            for skey in self.skey_list:
                if skey.hide_object:
                    self.skey_list.remove(skey)
            self.platform_list.update()
            self.monster_list.update()
            self.cship_list.update()
            self.skey_list.update()

        def draw(self, screen):
            # draw everything in level

            # draw the background
            screen.fill(WHITE)
            screen.blit(self.background,(self.world_shift // 200000000000000000000000000000000000000000,0))

            # draw the sprite lists
            self.platform_list.draw(screen)
            self.monster_list.draw(screen)
            self.cship_list.draw(screen)
            self.skey_list.draw(screen)

        def shift_world(self, shift_x):
            self.world_shift += shift_x
            for platform in self.platform_list:
                platform.rect.x += shift_x
            for monster in self.monster_list:
                monster.rect.x += shift_x
            for cship in self.cship_list:
                cship.rect.x += shift_x
            for skey in self.skey_list:
                skey.rect.x += shift_x


    # create platforms for the level
    class Level_01(Level):
        # definition level 1

        def __init__(self, mg_player):
            # Create level 1

            # call parent constructor
            Level.__init__(self, mg_player)
            self.background = pygame.image.load("resource/images/Stranded/davin_bg.png").convert()
            self.background.set_colorkey(WHITE)
            self.level_limit = -1000

            # width, height, x, and y of platform
            level = [[210, 70, 700, 700],
                     [600, 70, 000, 500],
                     [210, 70, 800, 300],
                     [9000, 70, 000, 830],   # Floor
                     [700, 900, -700, 000],  # Front wall
                     [100, 570, 1000, 300],
                     [100, 570, 1500, 300],
                     [600, 70, 1500, 300],
                     [100, 730, 2300, 000],
                     [500, 70, 1900, 660],
                     [70, 200, 1900, 460],
                     [300, 70, 1500, 550],
                     [20, 20, 1880, 710],
                     [20, 20, 2280, 500],
                     [700, 900, 9000, 000],  # Back Wall
                     [100, 800, 2700, 100],  # first pillar
                     [100, 30, 2600, 650],
                     [100, 30, 2600, 430],
                     [100, 30, 2600, 210],
                     [100, 650, 3200, 250],  # middle pillar
                     [100, 500, 3700, 400],  # 3rd pillar
                     [1000, 350, 4200, 550],
                     [80, 200, 4400, 350],
                     [200, 300, 5000, 250],
                     [80, 30, 4740, 200],
                     [1000, 100, 5000, 250],
                     [20, 10, 6180, 450],
                     [100, 700, 6200, 000],
                     #[900, 50, 5300, 650],
                     [500, 50, 6500, 780],
                     [500, 50, 6700, 580],
                     [500, 50, 6900, 380],
                     [500, 50, 7100, 180],
                     [600, 50, 7150, 630],
                     [600, 50, 7350, 430],
                     [600, 50, 7550, 230],
                     [500, 50, 7700, 580],
                     [500, 50, 7900, 380],
                     [500, 50, 8100, 180],
                     [50, 520, 8350, 380],
                     [50, 300, 8550, -100],
                     ]

            # go through the array above and add platforms
            for platform in level:
                block = Platform(platform[0], platform[1])
                block.rect.x = platform[2]
                block.rect.y = platform[3]
                block.MG_player = self.MG_player
                self.platform_list.add(block)

            # placing a Strandedkey block
            skey = Skey(43, 31)
            skey.rect.x = 8950
            skey.rect.y = 810 - 51
            skey.MG_player = self.MG_player
            self.skey_list.add(skey)


            # placing a ship block
            cship = Cship(290, 200)
            cship.rect.x = 0
            cship.rect.y = 237
            cship.MG_player = self.MG_player
            self.cship_list.add(cship)

            

            # placing the kill blocks beneath the pits
            monster = Monster(400, 50)
            monster.rect.x = 2800
            monster.rect.y = 830
            monster.MG_player = self.MG_player
            self.monster_list.add(monster)

            monster = Monster(400, 50)
            monster.rect.x = 3300
            monster.rect.y = 830
            monster.MG_player = self.MG_player
            self.monster_list.add(monster)

            #Kill block left of map
            monster = Monster(1000, 900)
            monster.rect.x = -1500
            monster.rect.y = 0
            monster.MG_player = self.MG_player
            self.monster_list.add(monster)
            #Kill block right of map
            monster = Monster(700, 100)
            monster.rect.x = 9000
            monster.rect.y = -100
            monster.MG_player = self.MG_player
            self.monster_list.add(monster)

            monster = Monster(400, 50)
            monster.rect.x = 3800
            monster.rect.y = 830
            monster.MG_player = self.MG_player
            self.monster_list.add(monster)

            # Add a custom moving enemy 1
            monster = MovingMonster(50, 75)
            monster.rect.x = 1500
            monster.rect.y = 225
            monster.boundary_left = 1500
            monster.boundary_right = 2050
            monster.change_x = 10
            monster.player = self.MG_player
            monster.level = self
            self.monster_list.add(monster)

            # Add a custom moving enemy 2
            monster = MovingMonster(50, 75)
            monster.rect.x = 1600
            monster.rect.y = 755
            monster.boundary_left = 1600
            monster.boundary_right = 2650
            monster.change_x = 5
            monster.player = self.MG_player
            monster.level = self
            self.monster_list.add(monster)

            # Add a custom moving enemy 3
            monster = MovingMonster(50, 75)
            monster.rect.x = 5300
            monster.rect.y = 755
            monster.boundary_left = 5200
            monster.boundary_right = 6450
            monster.change_x = 10
            monster.player = self.MG_player
            monster.level = self
            self.monster_list.add(monster)

            # Add a custom moving platform
            block = MovingPlatform(400, 20)
            block.rect.x = 1100
            block.rect.y = 310
            block.boundary_top = 310
            block.boundary_bottom = 830
            block.change_y = 4
            block.player = self.MG_player
            block.level = self
            self.platform_list.add(block)

            # Add another custom moving platform
            block = MovingPlatform(700, 10)
            block.rect.x = 5300
            block.rect.y = 650
            block.boundary_left = 5200
            block.boundary_right = 5500
            block.change_x = 10
            block.player = self.MG_player
            block.level = self
            self.platform_list.add(block)

            # another one
            block = MovingPlatform(250, 20)
            block.rect.x = 8400
            block.rect.y = 600
            block.boundary_top = 370
            block.boundary_bottom = 750
            block.change_y = 4
            block.player = self.MG_player
            block.level = self
            self.platform_list.add(block)


    def main():
        # main program
        pygame.init()

        # set height and width of screen
        size = [display_width, display_height]
        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Stranded")

        # create the MG_player
        mg_player = MG_Player()


        # create all levels
        level_list = []
        level_list.append(Level_01(mg_player))

        # set the current level
        current_level_no = 0
        current_level = level_list[current_level_no]

        active_sprite_list = pygame.sprite.Group()
        mg_player.level = current_level
        # loading in font
        font = pygame.font.SysFont('Arcadepix.ttf', 30)

        mg_player.rect.x = 20
        mg_player.rect.y = 800
        active_sprite_list.add(mg_player)

        # loop until closed
        global done
        done = False

        # how fast it updates
        clock = pygame.time.Clock()
        #score = 100000
        # main program loop
        while not done:
            time_alive = time.time() - startTime
            nonlocal score
            score = score - 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 5 and pygame.mouse.get_pos()[1] >= 5:
                        if pygame.mouse.get_pos()[0] <= 155 and pygame.mouse.get_pos()[1] <= 53:
                           score = 0
                           game_over.start(score, 5)
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        mg_player.go_left()
                    if event.key == pygame.K_RIGHT:
                        mg_player.go_right()
                    if event.key == pygame.K_UP:
                        mg_player.jump()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and mg_player.change_x < 0:
                        mg_player.stop()
                    if event.key == pygame.K_RIGHT and mg_player.change_x > 0:
                        mg_player.stop()
            # update the player
            active_sprite_list.update()

            # check collision

            # update items in the level
            current_level.update()

            # if the player goes near the right side move the world left
            if mg_player.rect.x >= 450:
                diff = mg_player.rect.x - 450
                mg_player.rect.x = 450
                current_level.shift_world(-diff)

            # if the player goes near the left side move world right
            if mg_player.rect.x <= 450:
                diff = 450 - mg_player.rect.x
                mg_player.rect.x = 450
                current_level.shift_world(diff)

            current_position = mg_player.rect.x + current_level.world_shift
            if current_position < current_level.level_limit:
                mg_player.rect.x = 450
                if current_level_no < len(level_list)-1:
                    current_level_no += 1
                    current_level = level_list[current_level_no]
                    MG_Player.level = current_level

            # level and sprite draw
            current_level.draw(screen)
            active_sprite_list.draw(screen)

            quit_button = pygame.transform.scale(
                pygame.image.load('resource/images/select_planet/button_quit_small.png'), (42, 40))
            quit_rect = quit_button.get_rect()
            screen.blit(quit_button, (5, 5))
            #Game over screen
            if done:
                print('game over')
                game_over.start(score, 5)
            font = pygame.font.Font("resource/fonts/Arcadepix.ttf", 30)
            scoretext = font.render("Score {0}".format(score), 1, WHITE)
            screen.blit(scoretext, (705, 10))
            if mg_player.rect.y < 0:
                playermarker = font.render("^^^".format(score), 1, GREEN)
                screen.blit(playermarker, (462, 10))
            objectivetext = font.render("Collect and retrieve the object!".format(score), 1, WHITE)
            screen.blit(objectivetext, (295, 855))
            scoretext = font.render("Time passed {0}".format(round(time_alive)), 1, WHITE)
            screen.blit(scoretext, (705, 30))
            # timer
            if score <= 0:
                pygame.quit()
            # limit to 30 frames per second
            clock.tick(30)

            # update the screen
            pygame.display.flip()
        # exit
        pygame.quit()

    main()
