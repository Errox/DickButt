#load in lybrary's
import pygame
import time
import os

#initialize pygame
pygame.init()

#define variables
size    = 600, 600
white   = 255, 255, 255
green   = 50, 255, 100
red     = 255, 0, 0

#get framerate

#set display of pygame
screen = pygame.display.set_mode(size)

def main():

    #define the rectangle 
    rectangle1X = 10
    rectangle1Y = 10
    rectangle1Width = 50
    rectangle1Heigh = 20
    rectangle1Color = red

    rectangle2X = 100
    rectangle2Y = 100
    rectangle2Width = 50
    rectangle2Heigh = 20
    rectangle2Color = green

    currentTime = time.clock()
    prevTime = currentTime
    frameRate = 1 / 60
    #running is always true unless else given
    running = True
    while running:
        #set framerate
        currentTime = time.clock()
        dt = currentTime - prevTime
        if(dt > frameRate):
            prevTime = currentTime
            
            #pumping all events to the main screen
            pygame.event.pump()
            #check if a button is pressed
            pressed = pygame.key.get_pressed()
            #clear screen with white
            screen.fill(white)

            #update the state S
            if pressed[pygame.K_LEFT]:
                rectangle1X = rectangle1X - 50
            if pressed[pygame.K_RIGHT]:
                rectangle1X = rectangle1X + 50
            if pressed[pygame.K_UP]:
                rectangle1Y = rectangle1Y - 50 
            if pressed[pygame.K_DOWN]:
                rectangle1Y = rectangle1Y + 50

            if pressed[pygame.K_a:
                rectangle2X = rectangle2X - 50
            if pressed[pygame.K_d]:
                rectangle2X = rectangle2X + 50
            if pressed[pygame.K_w]:
                rectangle2Y = rectangle2Y - 50 
            if pressed[pygame.K_s]:
                rectangle2Y = rectangle2Y + 50

            #draw S
            pygame.draw.rect(screen, rectangle1Color, (rectangle1X, rectangle1Y, rectangle1Width, rectangle1Heigh))
            pygame.draw.rect(screen, rectangle2Color, (rectangle2X, rectangle2Y, rectangle2Width, rectangle2Heigh))

            #if escape is pressed then quit
            if pressed[pygame.K_ESCAPE]:
                running = False

            # toggle = not toggle


            pygame.display.flip()
main()