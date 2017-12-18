import pygame
import time
from  pygame.locals import *

pygame.init()
FPS = 30
display_width = 900 
display_height = 900
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SpaceBound')
    #Colours!
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0,255,0)
grey = (100,100,100)

#Classes!
class SBMainCharacter(object): #It's you!
    def __init__(self,health,attack,x,y,w,h):
        self.health = health
        self.attack = attack
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw_char(self):
        pygame.draw.rect(gameDisplay, green, [self.x,self.y,self.w,self.h])

class SBenemy(object): #It's an enemy!
    def __init__(self, health, attack, x, y, w, h): #Add speed & movement
        self.health = health
        self.attack = attack
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw_enemy(self): #draw that enemy
        pygame.draw.rect(gameDisplay, red, [self.x,self.y,self.w,self.h]) #add sprite
    
    def attacked(self):
        self.health =- SBMainChar.attack

class SBEncounterTextBox(object):#All the text
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
        font = pygame.font.Font('../resource/fonts/ka1.ttf', 65)
        TextSurf = font.render(self.text, True, white)
        text_rect = TextSurf.get_rect()
        text_rect.center = ((display_width * 0.5), (display_height * 0.5))
        gameDisplay.blit(TextSurf, text_rect)

#Things from the classes
SBMainChar = SBMainCharacter(500, 50, ((display_width - 50) * 0.5), ((display_height - 75) * 0.5), 50, 75)
SBenemy1 = SBenemy(100, 10, 90, 90, 50, 75)
SBEncountertext = SBEncounterTextBox(0,0,700,100,"Encounter!")
SBFight = SBEncounterTextBox(675,600,110,30,"Fight")
SBMoves = SBEncounterTextBox(675,650,110,30,"Special Moves")
SBItems = SBEncounterTextBox(675,700,110,30,"Items")
SBRun = SBEncounterTextBox(675,750,110,30,"Run")
CharacterHealth = SBEncounterTextBox(425,700,50,30, "Health: %s"%(SBMainChar.health))
EnemyHealth = SBEncounterTextBox(425,10,50,30,"Health: %s"%(SBenemy1.health)) #Has to work on all enemies, not just enemy1


def SBEncounter(): #The actual encounter
    SBEncountertext.bigmessage_display() #Add encounter! Text. Has to disappear 
        #Add boxes around the text
    SBFight.addbox()
    SBMoves.addbox()
    SBItems.addbox()
    SBRun.addbox()
        #Add text
    SBFight.EncounterText()
    SBMoves.EncounterText()
    SBItems.EncounterText()
    SBRun.EncounterText()
    CharacterHealth.EncounterText()
    EnemyHealth.EncounterText()
    if SBenemy1.health <= 0:
        SBEncountering = False
    if SBMainChar.health <= 0:
        SpaceBound_Exit = True


def SBgame_loop():
    SBEncountering = False #Not in an encounter
    SpaceBound_Exit = False #The game is aliiiiive

    while not SpaceBound_Exit:
        pygame.event.pump()#Get them events
        if pygame.event.peek(pygame.QUIT): #Window is clicked away
                SpaceBound_Exit = True #Game is dead. You killed it.
        #While in an encounter        
        if SBEncountering:
                #Click the buttons
            if SBFight.EncounterText().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                print("clicked FIGHT")
                SBenemy1.attacked()
                time.sleep(1)
            if SBMoves.EncounterText().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                print("clicked MOVES")
                time.sleep(1)
            if SBItems.EncounterText().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                print("clicked ITEMS")
                time.sleep(1)
            if SBRun.EncounterText().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                print("clicked RUN")
                time.sleep(1)

        #while in the overworld
        if not SBEncountering:
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

           
            
        gameDisplay.fill(black) #gives the background a colour        
        SBMainChar.draw_char()        
        SBenemy1.draw_enemy()
                #Collision! Could probably use some work --> Needs to work on any enemy, not just enemy1
                    #Checks  the X coords for enemy1
        if SBMainChar.x > SBenemy1.x and SBMainChar.x < SBenemy1.x + SBenemy1.w or SBMainChar.x + SBMainChar.w > SBenemy1.x and SBMainChar.x + SBMainChar.w < SBenemy1.x + SBenemy1.w:
                    #Checks the y coords
            if SBMainChar.y > SBenemy1.y and SBMainChar.y < SBenemy1.y + SBenemy1.h or SBMainChar.y + SBMainChar.h > SBenemy1.y and SBMainChar.y + SBMainChar.h < SBenemy1.y + SBenemy1.h:
                SBEncountering = True
                SBEncounter()    #runs the encounter

        pygame.display.update()
        clock.tick(FPS)#Actually use the FPS

SBgame_loop()#Actually run the game
pygame.quit()
quit()



