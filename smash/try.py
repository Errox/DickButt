import pygame

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

    
    # initialize pygame and create window
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("INVATION OF THE UNKNOWN")
clock = pygame.time.Clock()
running = True
m1 = pygame.image.load('walk_4.png')
m2 = pygame.image.load('walk_8.png')

movingcurrent = 1

    # Game loop

while running:

        # keep loop running at the right speed
        # Process input (events)
    for event in pygame.event.get():
            # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if movingcurrent == 1:
            screen.blit(m1, (450, 450))
        if (movingcurrent == 2):
            screen.blit(m2, (450, 400)) 

        if  (movingcurrent >= 2):
            movingcurrent == 1
        else:
            movingcurrent += 1


        
    
    clock.tick(10)
             
        # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
quit()    

