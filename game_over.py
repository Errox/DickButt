
import sys
import pygame
import os
import menu
from time import sleep

FPS     = 30
X       = 500
Y       = 100
GREEN   = (0, 255, 0)
BLACK   = (0, 0, 0)

screen = pygame.display.set_mode((900,900))
pygame.display.set_caption("game_over")
clock = pygame.time.Clock()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
define_location = "main_menu"
    
#initializing pygame's mixer
# pygame.mixer.init()
# pygame.mixer.music.load("resource/music/main_menu/main_menu.ogg")
# pygame.mixer.music.play(-1)


def load_image(name):
    image = pygame.image.load(name)
    return image

class animated_select_planet(pygame.sprite.Sprite):
    def __init__(self):
        super(animated_select_planet, self).__init__()
        self.images = []
        self.images.append(load_image('resource/images/game_over/tekst/game_over_1.png'))
        self.images.append(load_image('resource/images/game_over/tekst/game_over_2.png'))
        self.images.append(load_image('resource/images/game_over/tekst/game_over_3.png'))
        self.images.append(load_image('resource/images/game_over/tekst/game_over_4.png'))
        self.images.append(load_image('resource/images/game_over/tekst/game_over_5.png'))
        self.images.append(load_image('resource/images/game_over/tekst/game_over_6.png'))
        self.images.append(load_image('resource/images/game_over/tekst/game_over_7.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(25, 130, 250, 80)

    def update(self):
        self.index += 1
        sleep(0.1)
        if self.index >= len(self.images):
            self.index = 0
            count = 0
        self.image = self.images[self.index]

#start the main menu board.
def start_game_over():
    #set background
    background = pygame.image.load('resource/images/game_over/game_overbg.png').convert()
    background_rect = background.get_rect()
    screen.blit(background, background_rect)
    buttons_game_over()

def buttons_game_over():
    quit_button         = pygame.image.load('resource/images/game_over/button_quit.png').convert()
    quit_rect           = quit_button.get_rect()
    screen.blit(quit_button, (325,550))

main_loop = True
my_sprite = animated_select_planet()
my_group = pygame.sprite.Group(my_sprite)
while main_loop:
    screen.fill(BLACK)
    clock.tick(FPS)
    start_game_over()
    my_group.update()
    my_group.draw(screen)

    for evento in pygame.event.get():
        #define event's of quiting the game.
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        #printing every event that's happening within the python script.
        print(evento)
        #Catch mouse position and if it's pressed on the button
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 315 and pygame.mouse.get_pos()[1] >= 550:
                if pygame.mouse.get_pos()[0] <= 593 and pygame.mouse.get_pos()[1] <= 615:
                    menu.start_menu()


    pygame.display.flip()

pygame.quit()
quit()
