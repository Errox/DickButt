
import pygame

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen size
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

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
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # if jump is possible change y speed
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -15

    # player movement speed
    def go_left(self):
        self.change_x = -14

    def go_right(self):
        self.change_x = 14

    def stop(self):
        self.change_x = 0


class Platform(pygame.sprite.Sprite):
    # platform layer can stand on

    def __init__(self, width, height):
        # platform constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()


class Level(object):
    # list of used sprites

    # camera moves with player
    world_shift = 0

    def __init__(self, mg_player):
        # constructor. pass in a handle to player
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.MG_player = mg_player

        # Background image
        self.background = None

    # update everything in level
    def update(self):
        # update everything in level
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        # draw everything in level

        # draw the background
        screen.fill(WHITE)

        # draw the sprite lists
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        self.world_shift += shift_x
        for platform in self.platform_list:
            platform.rect.x += shift_x
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


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
                 [100, 800, 2700, 100]
                 ]

        # go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.MG_player = self.MG_player
            self.platform_list.add(block)


def main():
    # main program
    pygame.init()

    # set height and width of screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Mario Galaxy")

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
    done = False

    # how fast it updates
    clock = pygame.time.Clock()

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

        # limit to 30 frames per second
        clock.tick(30)

        # update the screen
        pygame.display.flip()

    # exit
    pygame.quit()


if __name__ == "__main__":
    main()