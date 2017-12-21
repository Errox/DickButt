#   imports!
import pygame
import time
import random
from  pygame.locals import *
pygame.init()

#   things!
FPS = 30
display_width = 900 
display_height = 900
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SpaceBound')

#   Colours!
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0,255,0)
grey = (100,100,100)

#   Classes!
class SBMainCharacter(object):
    def __init__(self,health,attack,x,y,w,h):
        self.health = health
        self.attack = attack
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.kills = 0
        self.count = 0

    def draw_char(self):
        pygame.draw.rect(gameDisplay, green, [self.x,self.y,self.w,self.h])

    def scoring(self):
        scores = 100 * self.kills
    #   Endscore time added bonus: 10000000/(1000 + county)
        return scores

SBMainChar = SBMainCharacter(500, 50, ((display_width - 50) * 0.5), ((display_height - 75) * 0.5), 50, 75)

class SBEncounterTextBox(object):
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text

    def EncounterText(self):
        font = pygame.font.Font('../resource/fonts/Arcadepix.ttf', 20)
        TextSurf = font.render(self.text,True,white)
        text_rect = TextSurf.get_rect()
        text_rect.center = ((self.x + self.w * 0.5), (self.y + self.h * 0.5))
        gameDisplay.blit(TextSurf, text_rect)
        return text_rect

    def addbox(self):
        pygame.draw.rect(gameDisplay, grey, [self.x, self.y, self.w, self.h])

    
    def bigmessage_display(self):
        Encounterstart = False
        font = pygame.font.Font('../resource/fonts/ka1.ttf', 65)
        TextSurf = font.render(self.text, True, white)
        text_rect = TextSurf.get_rect()
        text_rect.center = ((display_width * 0.5), (display_height * 0.5))
        gameDisplay.blit(TextSurf, text_rect)

SBEncountertext = SBEncounterTextBox(0,0,700,100,"Encounter!")
SBFight = SBEncounterTextBox(675,500,110,30,"    Fight    ")
SBMoves = SBEncounterTextBox(675,550,110,30,"Special Moves")
SBItems = SBEncounterTextBox(675,600,110,30,"    Items    ")
SBRun = SBEncounterTextBox(675,650,110,30,  "     Run     ")

class SBenemy(object):
    def __init__(self, health, attack, x, y, w, h, alive): #Gotta add speed & movement
        self.health = health
        self.attack = attack
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.alive = alive
        self.timer = 0
        self.Your_Turn = True
        self.SBEncountering = False

    def draw_enemy(self):
        if self.alive == True:
            pygame.draw.rect(gameDisplay, red, [self.x,self.y,self.w,self.h])

    def Encounter(self):
    #           Collision
        if SBMainChar.x > self.x and SBMainChar.x < self.x + self.w or SBMainChar.x + SBMainChar.w > self.x and SBMainChar.x + SBMainChar.w < self.x + self.w:
            if SBMainChar.y > self.y and SBMainChar.y < self.y + self.h or SBMainChar.y + SBMainChar.h > self.y and SBMainChar.y + SBMainChar.h < self.y + self.h:
                if self.timer <= FPS:
                    SBEncountertext.bigmessage_display()
                    self.timer += 1
                    self.SBEncountering = True
                if self.timer >= FPS:
                    if self.SBEncountering == True:
                        (SBEncounterTextBox(425,10,50,30,"Enemy Health: " + str(self.health))).EncounterText()
    #                       When does the combat end
                        if self.health <= 0:
                            self.SBEncountering = False
                            self.timer = 0
                        if SBMainChar.health <= 0:
                            SpaceBound_Exit = True
    #                       Your turn
                        if self.Your_Turn == True:
                            SBFight.addbox()
                            SBMoves.addbox()
                            SBItems.addbox()
                            SBRun.addbox()
                            SBFight.EncounterText()
                            SBMoves.EncounterText()
                            SBItems.EncounterText()
                            SBRun.EncounterText()

                            if SBFight.EncounterText().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                self.attacked()
                                print("You attacked!")
                                self.Your_Turn = False
                                if not self.alive:
                                    self.SBEncountering = False
                                    SBMainChar.kills += 1
                            if SBMoves.EncounterText().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                print("WIP")
                                self.Your_Turn = False
                            if SBItems.EncounterText().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                print("WIP")
                                self.Your_Turn = False
                            if SBRun.EncounterText().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                if random.randint(0,100) < 75:
                                    self.SBEncountering = False
                                    self.timer = 0
                                    print("Escape succesfull")
                                else:
                                    print("Escape unsuccesfull")
                                self.Your_Turn = False
    #                            Enemy's turn
                        if not self.Your_Turn:
                            time.sleep(1) 
                            self.attacking()
                            print("Enemy attacked!")
                            self.Your_Turn = True
  
    def attacked(self):
        self.health = self.health - SBMainChar.attack
        if self.health <= 0:
            self.die()
    
    def attacking(self):
        SBMainChar.health = SBMainChar.health - self.attack
    
    def die(self):
        self.alive = False

    def Encountering(self):
        return self.SBEncountering

SBenemy1 = SBenemy(100, 10, 90, 90, 50, 75, True)
SBenemy2 = SBenemy(150, 15, 810, 90, 50, 75, True)

def SBgame_loop():
    
    SpaceBound_Exit = False
    timer2 = 0

    while not SpaceBound_Exit:
        CharacterHealth = SBEncounterTextBox(425,700,50,30, "Health: " + str(SBMainChar.health))
        Score = SBEncounterTextBox(800,5,100,30,"Score: " + str(int(SBMainChar.scoring())))
        
        pygame.event.pump()
        if pygame.event.peek(pygame.QUIT): 
                SpaceBound_Exit = True

#           while in the overworld

        SBenemy1.Encountering()
        SBenemy2.Encountering()
        if not SBenemy1.Encountering()and not SBenemy2.Encountering():
            if pygame.key.get_pressed()[pygame.K_a]:
                SBleft = -10 #To the left
                if SBMainChar.x < 0:
                    SBleft = 0 #Don't move off the screen
                SBMainChar.x += SBleft #Actually move
            if pygame.key.get_pressed()[pygame.K_d]:
                SBright = 10 #To the right
                if SBMainChar.x > display_width - SBMainChar.w:
                    SBright = 0
                SBMainChar.x += SBright
            if pygame.key.get_pressed()[pygame.K_w]:
                SBup = -10 #Going up
                if SBMainChar.y < 0:
                    SBup = 0
                SBMainChar.y += SBup
            if pygame.key.get_pressed()[pygame.K_s]:
                SBdown = 10 #Going down
                if SBMainChar.y > display_height - SBMainChar.h:
                    SBdown = 0
                SBMainChar.y += SBdown
            
#       Create the world
        gameDisplay.fill(black) #gives the background a colour   
        Score.EncounterText()     
        SBMainChar.draw_char()    
#       Draw the enemies            
        SBenemy1.draw_enemy()
        SBenemy2.draw_enemy()
        CharacterHealth.EncounterText()

        SBenemy1.Encounter()
        SBenemy2.Encounter()

        SBMainChar.count += 1
        pygame.display.update()
        clock.tick(FPS)
    # end of while loop

SBgame_loop()#Actually run the game
pygame.quit()
quit()



