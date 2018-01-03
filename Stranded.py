
def start_stranded():
    import pygame
    import menu


    # Global constants

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BEIGE = (255,211,155)
    BROWN = (139,125,107)

    # Screen size
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 900

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
            self.image = pygame.Surface([width, height])
            self.image.fill(GREEN)

            self.rect = self.image.get_rect()

            # set speed of mg_player
            self.change_x = 0
            self.change_y = 0

            # list of sprites to walk against
            self.level = None
            # Inventory
            self.inventory = None

        def update(self):
            # move the player
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
                global done
                done = True
                # if moving right
                # set right side to left if object is hit
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                elif self.change_x < 0:
                    # set left side to right side
                    self.rect.left = block.rect.right

            # move up and down
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
                self.inventory = True
                block.hide()

        # calculating gravity
        def calc_grav(self):

            if self.change_y == 0:
                self.change_y = 10
            else:
                self.change_y += .50

            # check if ground bellow player
            if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = SCREEN_HEIGHT - self.rect.height

        def jump(self):
            # check if there is ground bellow so that the MG_Player can jump
            self.rect.y += 5
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y -= 5

            self.rect.y += 5
            monster_hit_list = pygame.sprite.spritecollide(self, self.level.monster_list, False)
            self.rect.y -= 5

            # if jump is possible change y speed
            if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
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

            self.image = pygame.Surface([width, height])
            self.image.fill(RED)

            self.rect = self.image.get_rect()


    class Cship(pygame.sprite.Sprite):
        # Cship (crashed ship) the drop of point

        def __init__(self, width, height):
            # Cship constructor
            super().__init__()

            self.image = pygame.Surface([width, height])
            self.image.fill(BEIGE)

            self.rect = self.image.get_rect()


    class Skey(pygame.sprite.Sprite):
        # Skey (StrandedKey) the pick up point

        def __init__(self, width, height):
            # Skey constructor
            super().__init__()

            self.image = pygame.Surface([width, height])
            self.image.fill(BROWN)

            self.rect = self.image.get_rect()
            # SHow by default
            self.hide_object = False

        def hide(self):
            # Block has been captured
            self.hide_object = True


    class Platform(pygame.sprite.Sprite):
        # platform layer can stand on

        def __init__(self, width, height):
            # platform constructor
            super().__init__()

            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)

            self.rect = self.image.get_rect()


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
                     [900, 50, 5300, 650],
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
                     [400, 20, 8600, 380],
                     [20, 220, 8600, 380],
                     [400, 20, 8600, 810]
                     ]

            # go through the array above and add platforms
            for platform in level:
                block = Platform(platform[0], platform[1])
                block.rect.x = platform[2]
                block.rect.y = platform[3]
                block.MG_player = self.MG_player
                self.platform_list.add(block)

            # placing a Strandedkey block
            skey = Skey(100, 100)
            skey.rect.x = 8750
            skey.rect.y = 710
            skey.MG_player = self.MG_player
            self.skey_list.add(skey)

            # placing a test ship block
            cship = Cship(400, 150)
            cship.rect.x = 0
            cship.rect.y = 350
            cship.MG_player = self.MG_player
            self.cship_list.add(cship)

            # placing a test kill block
            monster = Monster(50, 50)
            monster.rect.x = 200
            monster.rect.y = 200
            monster.MG_player = self.MG_player
            self.monster_list.add(monster)

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

            monster = Monster(400, 50)
            monster.rect.x = 3800
            monster.rect.y = 830
            monster.MG_player = self.MG_player
            self.monster_list.add(monster)

            # Add a custom moving platform
            block = MovingPlatform(400, 20)
            block.rect.x = 1100
            block.rect.y = 300
            block.boundary_top = 300
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
            block = MovingPlatform(200, 20)
            block.rect.x = 8400
            block.rect.y = 600
            block.boundary_top = 370
            block.boundary_bottom = 830
            block.change_y = 4
            block.player = self.MG_player
            block.level = self
            self.platform_list.add(block)


    def main():
        # main program
        pygame.init()

        # set height and width of screen
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
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

        mg_player.rect.x = 20
        mg_player.rect.y = 800
        active_sprite_list.add(mg_player)

        # loop until closed
        global done
        done = False

        # how fast it updates
        clock = pygame.time.Clock()
        # there are 3600 clocks, 30 a second so 120 second or 2 minutes
        start = 3600

        # main program loop
        while not done:
            for event in pygame.event.get():
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
            # timer
            start -= 1
            if start <= 0:
                pygame.quit()
            # limit to 30 frames per second
            clock.tick(30)

            # update the screen
            pygame.display.flip()

        # exit
        pygame.quit()


    if __name__ == "__main__":
        main()
