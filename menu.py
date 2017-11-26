import pygame
FPS = 30
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
pygame.init();
screen = pygame.display.set_mode((900,900));
pygame.display.set_caption("menu");
menuAtivo = True;
clock = pygame.time.Clock()


background = pygame.image.load('astrodoge/img/backgrounds/background_2.png').convert()
background_rect = background.get_rect()
pygame.mixer.init()
pygame.mixer.music.load("astrodoge/music/main_menu.ogg")
pygame.mixer.music.play(-1)

screen.fill(BLACK)
screen.blit(background, background_rect)

def startGame():
    screen.fill(GREEN);
    pygame.display.flip();

while menuAtivo:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
               pygame.quit();
        print(evento);
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 230:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
                        menuAtivo = False
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 90:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 140:
                        startGame();

    start_button = pygame.draw.rect(screen,(0,0,240),(150,90,100,50));
    
    quit_button = pygame.draw.rect(screen,(244,0,0),(150,230,100,50));

    pygame.display.flip();

pygame.quit()