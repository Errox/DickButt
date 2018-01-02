#this scripts is a big mixer for all sounds and other musical stuff to all keep it simple and in theme 
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
    
def bullet_shoot_friendly():
    bullet = pygame.mixer.Sound('resource/soundboard/shoot/friendly/sfx_1.ogg')
    bullet.set_volume(0.5)
    bullet.play()
    
def bullet_on_hit_enemy():

    random_1 = random.randint(0, 100)
    if random_1 >= 81:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/enemy/hit_1.wav')
    elif random_1 >= 0 and random_1 <= 20:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/enemy/hit_2.wav')
    elif random_1 >= 21 and random_1 <= 40:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/enemy/hit_3.wav')
    elif random_1 >= 41 and random_1 <= 60:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/enemy/hit_4.wav')
    elif random_1 >= 61 and random_1 <= 80:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/enemy/hit_5.wav')
    bullet.set_volume(0.5)
    bullet.play()

def bullet_on_hit_friendly():
    random_1 = random.randint(0, 60)
    if random_1 >= 41:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/friendly/hit_1.wav')
    elif random_1 >= 0 and random_1 <= 20:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/friendly/hit_2.wav')
    elif random_1 >= 21 and random_1 <= 40:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/friendly/hit_3.wav')
    bullet.set_volume(0.5)
    bullet.play()

