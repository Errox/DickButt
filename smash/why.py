import pygame
import os
import random

pygame.init()
mainClock = pygame.time.Clock()

#Color coding 
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
RED = (225, 0, 0)
BLUE = (0, 0, 255 )
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)


#difine game core
WIDTH = 900
HIGHT = 900

pygameScreen = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption('SUMO SMASH')


#objects 
x = 430
y = 500
player = pygame.Rect(x, y, 50, 30)
enemy_player = pygame.Rect(430, 300, 50, 30)

# my images location ' img = pygame.image.load('sumo_ring.png').convert()

#My main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.type == pygame.K_RIGHT:
                x += 20

    pygameScreen.fill(WHITE)
    pygame.draw.rect(pygameScreen, PURPLE, player)
    pygame.draw.rect(pygameScreen, GREEN, enemy_player)
    pygame.display.update()

# hij moet terugkeren naar het beginpunt
if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                sumo_x == WIDTH/2


#block to go up and down
            if event.key == pygame.K_UP:
                sumo_y = -10
            if event.key == pygame.K_DOWN:
                sumo_y = 10

    