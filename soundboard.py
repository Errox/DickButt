import pygame
import sys
import os
import platform
import random

pygame.init()
pygame.mixer.init()

#check if there is already a sound playing. Else fade the current one out


#all music functions
def main_menu():
    pygame.mixer.music.load('resource/soundboard/music/main_menu/main_menu.ogg')
    pygame.mixer.music.play(1)

#sequence when game_over scene is triggered
def game_over(score):
    print(score)
    if score == 0:
        pygame.mixer.music.load('resource/soundboard/music/game_over/game_over_0.ogg')
    else:
        #randomizer on death
        random_1 = random.randint(0, 100)
        if random_1 >= 90:
            pygame.mixer.music.load('resource/soundboard/music/game_over/game_over_95.ogg')
        elif random_1 >= 0 and random_1 <= 10:
            pygame.mixer.music.load('resource/soundboard/music/game_over/game_over_85.ogg')
        else:
            pygame.mixer.music.load('resource/soundboard/music/game_over/game_over.ogg')
    pygame.mixer.music.play(1)

#define pause
def pause():
    pygame.mixer.music.pause()


#Astrododge main. 
def ast_main():
    pygame.mixer.music.load('resource/soundboard/music/astrododge/song_1.ogg')
    pygame.mixer.music.queue('resource/soundboard/music/astrododge/song_2.ogg')
    pygame.mixer.music.queue('resource/soundboard/music/astrododge/song_3.ogg')
    pygame.mixer.music.play(-1)
    


    
    
