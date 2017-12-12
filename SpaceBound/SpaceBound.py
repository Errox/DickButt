import pygame
import time
pygame.init()
FPS = 30 #frames per sec and such
            #PAS ALLES AAN MET SB ERVOOR. defs, vars, classes
display_width = 900 
display_height = 900

#Colours!
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0,255,0)
grey = (100,100,100)

gameDisplay = pygame.display.set_mode((display_width, display_height)) #The Screen!
pygame.display.set_caption('SpaceBound') #Caption
clock = pygame.time.Clock() #It's a clock!

SBcharImg = pygame.image.load('SBimages/temp_character.png') #Load character model

def SBchar(xChar,yChar): #Create a character, might change later to draw it
    gameDisplay.blit(SBcharImg,(xChar,yChar))
def SBenemy(xEnemy,yEnemy,wEnemy,hEnemy,colour): #Draw an enemy
    pygame.draw.rect(gameDisplay, colour, [xEnemy,yEnemy,wEnemy,hEnemy])
#I could draw a circle as detection circle thingy
def SBEncounterBox(xBox, yBox, wBox, hBox, colour, text):
    pygame.draw.rect(gameDisplay, colour, [xBox, yBox, wBox, hBox])
    SB_EncounterBox_message_display(xBox, yBox, hBox, wBox, text)
    pygame.display.update()

def SBtext_objects(text, font): #helps with the text thing
    SBTextSurf = font.render(text, True, white)
    return SBTextSurf, SBTextSurf.get_rect()

def SB_EncounterBox_message_display(xBox, yBox, hBox, wBox, text):
    SBtextText = pygame.font.Font('../resource/fonts/Arcadepix.ttf', 20)
    SBText_Surf, SBText_Rect = SBtext_objects(text, SBtextText)
    SBText_Rect.center = ((xBox + wBox * 0.5), (yBox + hBox * 0.5))
    gameDisplay.blit(SBText_Surf, SBText_Rect)
    pygame.display.update()

def SBbigmessage_display(text): #does the text thing
    SBEncounterText = pygame.font.Font('../resource/fonts/ka1.ttf', 65)
    SBTextSurf, SBTextRect = SBtext_objects(text, SBEncounterText)
    SBTextRect.center = ((display_width * 0.5), (display_height * 0.5))
    gameDisplay.blit(SBTextSurf, SBTextRect)
    pygame.display.update()

def SBEncounter(): #The actual encounter
    SBbigmessage_display('Encounter!')
    time.sleep(2)
    SBEncountering = True
    SBEncounterBox(display_width*0.75, display_height*0.60, 110, 30, grey, 'Fight')
    SBEncounterBox(display_width*0.75, display_height*0.65, 110, 30, grey, 'Special moves')
    SBEncounterBox(display_width*0.75, display_height*0.70, 110, 30, grey, 'Items')
    SBEncounterBox(display_width*0.75, display_height*0.75, 110, 30, grey, 'Run')

    
    #SBgame_loop() #For now, restarts the game



def SBgame_loop():
    SBxChar = ((display_width - 50) * 0.5)
    SByChar = ((display_height - 75) * 0.5)

    SBxEnemystart = (display_width * 0.1) 
    SByEnemystart = (display_height * 0.1)
    SBEnemyspeed = 7 #not in use atm
    SBwEnemy = 50
    SBhEnemy = 75
    SBEncountering = False

    SpaceBound_Exit = False #The game is aliiiiive

    while not SpaceBound_Exit:
        pygame.event.pump()#Get them events
        if pygame.event.peek(pygame.QUIT): #Window is clicked away
                SpaceBound_Exit = True #Game is dead. You killed it.
            #MOVEMENT 

        if pygame.key.get_pressed()[pygame.K_a]:
            SBleft = -10 #To the left
            if SBxChar < 0:
                SBleft = 0 #Don't move off the screen
            SBxChar += SBleft #Actually move
        if pygame.key.get_pressed()[pygame.K_d]:
            SBright = 10 #To the right
            if SBxChar > display_width - 50: #The 50 stands for the width
                SBright = 0
            SBxChar += SBright
        if pygame.key.get_pressed()[pygame.K_w]:
            SBup = -10 #Going up
            if SByChar < 0:
                SBup = 0
            SByChar += SBup
        if pygame.key.get_pressed()[pygame.K_s]:
            SBdown = 10 #Going down
            if SByChar > display_height - 75: #The 75 stands for the height
                SBdown = 0
            SByChar += SBdown
            
        gameDisplay.fill(black) #gives the background a colour        
        SBenemy(SBxEnemystart,SByEnemystart,SBwEnemy,SBhEnemy,red)#Spawns an enemy, will add movement later
        SBchar(SBxChar,SByChar) #spawns the character



                #Collision! Could probably use some work
                    #Checks  the X coords
        if SBxChar > SBxEnemystart and SBxChar < SBxEnemystart + SBwEnemy or SBxChar + 50 > SBxEnemystart and SBxChar + 50 < SBxEnemystart + SBwEnemy:
                    #Checks the y coords
            if SByChar > SByEnemystart and SByChar < SByEnemystart + SBhEnemy or SByChar + 75 > SByEnemystart and SByChar + 75 < SByEnemystart + SBhEnemy:
                SBEncounter()#runs the encounter

        
        pygame.display.update()#Updates the screen to what's happening
        clock.tick(FPS)#Actually use the FPS

SBgame_loop()#Actually run the game
pygame.quit()#quit it
quit()#quit it x2



