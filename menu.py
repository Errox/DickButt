import pygame


pygame.init();
screen = pygame.display.set_mode((400,300));
pygame.display.set_caption("menu");
menuAtivo = True;

start_button = pygame.draw.rect(screen,(0,0,240),(150,90,100,50));
continue_button = pygame.draw.rect(screen,(0,244,0),(150,160,100,50));
quit_button = pygame.draw.rect(screen,(244,0,0),(150,230,100,50));


pygame.display.flip();

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def startGame():
    screen.fill((0,0,0));
    pygame.display.flip();
    import nemesis.py;

BackGround = Background('img/backgrounds/Background_94.png', [0,10])
while menuAtivo:
    for evento in pygame.event.get():
        print(evento);
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 230:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
                        pygame.quit();
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 90:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 140:
                        startGame();

    screen.blit(BackGround.image, BackGround.rect)