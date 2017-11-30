import pygame
FPS = 30
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((900,900))
pygame.display.set_caption("Prototype")
menuAtivo = True
clock = pygame.time.Clock()

background = pygame.image.load('resource/images/main_menu/main_menu.png').convert()
background_rect = background.get_rect()
pygame.mixer.init()
pygame.mixer.music.load("astrodoge/music/main_menu.ogg")
# pygame.mixer.music.play(-1)

screen.fill(BLACK)
screen.blit(background, background_rect)

def startGame():
    background_1 = pygame.image.load('resource/images/main_menu/main_menu.png').convert()
    background_rect = background.get_rect()
    screen.blit(background_1, background_rect)
    pygame.display.flip()

def main_menu_buttons():
    quit_button = pygame.image.load('resource/images/main_menu/button_quit.png').convert()
    quit_rect = quit_button.get_rect()
    screen.blit(quit_button, (330, 600))
    highscore_button = pygame.image.load('resource/images/main_menu/button_high_score.png').convert()
    highscore_rect = highscore_button.get_rect()
    screen.blit(highscore_button, (330,450))
    credits_button = pygame.image.load('resource/images/main_menu/button_credits.png').convert()
    credits_rect = credits_button.get_rect()
    screen.blit(credits_button, (330,525))
    start_button = pygame.image.load('resource/images/main_menu/button_play_game.png').convert()
    start_rect = start_button.get_rect()
    screen.blit(start_button, (330,380))

def texts(text, x, y):
    font = pygame.font.Font("resource/fonts/Arcadepix.ttf",30)
    text = font.render(str(text), 1,(255,255,255))
    screen.blit(text, (x, y))

while menuAtivo:
    clock.tick(FPS)
    main_menu_buttons()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
               pygame.quit()
        print(evento);
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 330 and pygame.mouse.get_pos()[1] >= 380:
                if pygame.mouse.get_pos()[0] <= 598 and pygame.mouse.get_pos()[1] <= 445:
                        startGame()
                        texts("You've pressed start!", 330, 700)
            if pygame.mouse.get_pos()[0] >= 330 and pygame.mouse.get_pos()[1] >= 600:
                if pygame.mouse.get_pos()[0] <= 600 and pygame.mouse.get_pos()[1] <= 665:
                        menuAtivo = False

    pygame.display.flip()

pygame.quit()