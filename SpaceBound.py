def start_SpaceBound():
#   imports!        
    import pygame
    import menu
    import time
    import random
    import pygame.locals
    import game_over
    pygame.init()
#   things!
    FPS = 30
    display_width = 900 
    display_height = 900
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('SpaceBound')
#   Images
    Backgroundimg = pygame.image.load('resource/images/SpaceBound/Background_SpaceBound.gif')
    Obj_act = pygame.image.load('resource/images/SpaceBound/Objective_active.png')
    Obj_inact = pygame.image.load('resource/images/SpaceBound/Objective_inactive.png')
    Quit_Butt = pygame.image.load('resource/images/select_planet/button_quit_small.png')
#   Healimg
    Healsimg = pygame.image.load('resource/images/SpaceBound/Heals/Heals.png')
    Heal1img = pygame.image.load('resource/images/SpaceBound/Heals/Heal1.png')
    Heal2img = pygame.image.load('resource/images/SpaceBound/Heals/Heal2.png')
    Heal3img = pygame.image.load('resource/images/SpaceBound/Heals/Heal3.png')
    Heal4img = pygame.image.load('resource/images/SpaceBound/Heals/Heal4.png')
    Heal5img = pygame.image.load('resource/images/SpaceBound/Heals/Heal5.png')
    Heal6img = pygame.image.load('resource/images/SpaceBound/Heals/Heal6.png')
    Heal7img = pygame.image.load('resource/images/SpaceBound/Heals/Heal7.png')
    Heal8img = pygame.image.load('resource/images/SpaceBound/Heals/Heal8.png')
    Heal9img = pygame.image.load('resource/images/SpaceBound/Heals/Heal9.png')
    Heal10img = pygame.image.load('resource/images/SpaceBound/Heals/Heal10.png')
    Heal11img = pygame.image.load('resource/images/SpaceBound/Heals/Heal11.png')
#   Rightimg
    MC_Stance_1R = pygame.image.load('resource/images/Character/Purple/Right/Stance/1.png')
    MC_Stance_2R = pygame.image.load('resource/images/Character/Purple/Right/Stance/2.png')
    MC_run_1R = pygame.image.load('resource/images/Character/Purple/Right/Run/1.png')
    MC_run_2R = pygame.image.load('resource/images/Character/Purple/Right/Run/2.png')
    MC_run_3R = pygame.image.load('resource/images/Character/Purple/Right/Run/3.png')
    MC_run_4R = pygame.image.load('resource/images/Character/Purple/Right/Run/4.png')
    MC_run_5R = pygame.image.load('resource/images/Character/Purple/Right/Run/5.png')
    MC_run_6R = pygame.image.load('resource/images/Character/Purple/Right/Run/6.png')
    MC_run_7R = pygame.image.load('resource/images/Character/Purple/Right/Run/7.png')
    MC_run_8R = pygame.image.load('resource/images/Character/Purple/Right/Run/8.png')
    MC_run_9R = pygame.image.load('resource/images/Character/Purple/Right/Run/9.png')
#   Leftimg
    MC_Stance_1l = pygame.image.load('resource/images/Character/Purple/Left/Stance/1.png')
    MC_Stance_2l = pygame.image.load('resource/images/Character/Purple/Left/Stance/2.png')
    MC_run_1l = pygame.image.load('resource/images/Character/Purple/Left/Run/1.png')
    MC_run_2l = pygame.image.load('resource/images/Character/Purple/Left/Run/2.png')
    MC_run_3l = pygame.image.load('resource/images/Character/Purple/Left/Run/3.png')
    MC_run_4l = pygame.image.load('resource/images/Character/Purple/Left/Run/4.png')
    MC_run_5l = pygame.image.load('resource/images/Character/Purple/Left/Run/5.png')
    MC_run_6l = pygame.image.load('resource/images/Character/Purple/Left/Run/6.png')
    MC_run_7l = pygame.image.load('resource/images/Character/Purple/Left/Run/7.png')
    MC_run_8l = pygame.image.load('resource/images/Character/Purple/Left/Run/8.png')
    MC_run_9l = pygame.image.load('resource/images/Character/Purple/Left/Run/9.png')
#   Alienimg
    AB1 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Back/1.png')
    AB2 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Back/2.png')
    AB3 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Back/3.png')

    AF0 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Front/0.png')
    AF1 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Front/1.png')
    AF2 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Front/2.png')
    AF3 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Front/3.png')

    AL0 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Left/0.png')
    AL1 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Left/1.png')
    AL2 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Left/2.png')
    AL3 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Left/3.png')

    ALB1 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Left_Back/1.png')
    ALB2 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Left_Back/2.png')
    ALB3 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Left_Back/3.png')

    ALF0 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Left_Front/0.png')
    ALF1 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Left_Front/1.png')
    ALF2 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Left_Front/2.png')
    ALF3 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Left_Front/3.png')

    AR0 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Right/0.png')
    AR1 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Right/1.png')
    AR2 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Right/2.png')
    AR3 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Right/3.png')

    ARB1 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Right_Back/1.png')
    ARB2 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Right_Back/2.png')
    ARB3 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Right_Back/3.png')

    ARF0 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Right_Front/0.png')
    ARF1 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Right_Front/1.png')
    ARF2 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Right_Front/2.png')
    ARF3 = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Right_Front/3.png')

    AlienDead = pygame.image.load('resource/images/SpaceBound/Aliens/Alien/Dead.png')
#   Colours!
    black = (0,0,0)
    white = (255,255,255)
    red = (255, 0, 0)
    green = (0,255,0)
    blue = (0,0,255)
    grey = (100,100,100)
    gray = (50,50,50)
#   Main Character
    class SBMainCharacter(pygame.sprite.Sprite):
        def __init__(self,health,attack,x,y,w,h,stam):
            self.health = health
            self.attack = attack
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.stam = stam
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            self.kills = 0
            self.count = 0
            self.sprite = True
            self.run = 1
            self.timer = 0
            self.running = False
            self.direction = "right"

        def draw_char(self):
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        #   Standing still
            if not self.running:
                if self.direction == "right":
                    if self.sprite:
                        gameDisplay.blit(MC_Stance_1R, (self.x,self.y))
                        self.timer += 1
                        if self.timer == 10:
                            self.sprite = False
                    else:
                        gameDisplay.blit(MC_Stance_2R, (self.x,self.y))
                        self.timer -= 1
                        if self.timer == 0:
                            self.sprite = True
                if self.direction == "left":
                    if self.sprite:
                        gameDisplay.blit(MC_Stance_1l, (self.x,self.y))
                        self.timer += 1
                        if self.timer == 10:
                            self.sprite = False
                    else:
                        gameDisplay.blit(MC_Stance_2l, (self.x,self.y))
                        self.timer -= 1
                        if self.timer == 0:
                            self.sprite = True
        #   Moving
            else:
                if self.direction == "right":
                    if self.run >= 0 and self.run < 5:
                        gameDisplay.blit(MC_run_1R, (self.x,self.y))
                        self.run += 1
                    if self.run >= 5 and self.run < 10:
                        gameDisplay.blit(MC_run_2R, (self.x,self.y))
                        self.run += 1
                    if self.run >= 10 and self.run < 15:
                        gameDisplay.blit(MC_run_3R, (self.x,self.y))
                        self.run += 1
                    if self.run >= 15 and self.run < 20:
                        gameDisplay.blit(MC_run_4R, (self.x,self.y))
                        self.run += 1
                    if self.run >= 20 and self.run < 25:
                        gameDisplay.blit(MC_run_5R, (self.x,self.y))
                        self.run += 1
                    if self.run >= 25 and self.run < 30:
                        gameDisplay.blit(MC_run_6R, (self.x,self.y))
                        self.run += 1
                    if self.run >= 30 and self.run < 35:
                        gameDisplay.blit(MC_run_7R, (self.x,self.y))
                        self.run += 1
                    if self.run >= 35 and self.run < 40:
                        gameDisplay.blit(MC_run_8R, (self.x,self.y))
                        self.run += 1
                    if self.run >= 40 and self.run < 45:
                        gameDisplay.blit(MC_run_9R, (self.x,self.y))
                        self.run += 1
                    if self.run == 45:
                        self.run = 0
                if self.direction == "left":
                    if self.run >= 0 and self.run < 5:
                        gameDisplay.blit(MC_run_1l, (self.x,self.y))
                        self.run += 1
                    if self.run >= 5 and self.run < 10:
                        gameDisplay.blit(MC_run_2l, (self.x,self.y))
                        self.run += 1
                    if self.run >= 10 and self.run < 15:
                        gameDisplay.blit(MC_run_3l, (self.x,self.y))
                        self.run += 1
                    if self.run >= 15 and self.run < 20:
                        gameDisplay.blit(MC_run_4l, (self.x,self.y))
                        self.run += 1
                    if self.run >= 20 and self.run < 25:
                        gameDisplay.blit(MC_run_5l, (self.x,self.y))
                        self.run += 1
                    if self.run >= 25 and self.run < 30:
                        gameDisplay.blit(MC_run_6l, (self.x,self.y))
                        self.run += 1
                    if self.run >= 30 and self.run < 35:
                        gameDisplay.blit(MC_run_7l, (self.x,self.y))
                        self.run += 1
                    if self.run >= 35 and self.run < 40:
                        gameDisplay.blit(MC_run_8l, (self.x,self.y))
                        self.run += 1
                    if self.run >= 40 and self.run < 45:
                        gameDisplay.blit(MC_run_9l, (self.x,self.y))
                        self.run += 1
                    if self.run == 45:
                        self.run = 0

        def scoring(self):
            scores = 1000 * self.kills + self.count
            return scores

    SBMainChar = SBMainCharacter(250, 10, 425, 410, 50, 75, 100)
#   Texts
    class SBEncounterTextBox(object):
        def __init__(self, x, y, w, h, text):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.text = text
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        def EncounterText(self):
            font = pygame.font.Font('resource/fonts/Arcadepix.ttf', 20)
            TextSurf = font.render(self.text,True,white)
            text_rect = TextSurf.get_rect()
            text_rect.center = ((self.x + self.w * 0.5), (self.y + self.h * 0.5))
            gameDisplay.blit(TextSurf, text_rect)
            return text_rect

        def Battlelogtext(self):
            font = pygame.font.Font('resource/fonts/Arcadepix.ttf', 20)
            TextSurf = font.render(self.text,True,white)
            text_rect = (self.x, self.y, self.w, self.h)
            gameDisplay.blit(TextSurf, text_rect)
            return text_rect

        def addbox(self):
            pygame.draw.rect(gameDisplay, grey, [self.x, self.y, self.w, self.h])
            return self.rect

        
        def bigmessage_display(self):
            Encounterstart = False
            font = pygame.font.Font('resource/fonts/ka1.ttf', 65)
            TextSurf = font.render(self.text, True, white)
            text_rect = TextSurf.get_rect()
            text_rect.center = ((display_width * 0.5), (display_height * 0.5))
            gameDisplay.blit(TextSurf, text_rect)

    SBEncountertext = SBEncounterTextBox(0,0,700,100,"Encounter!")
   # Encounter blocks
    SBFight = SBEncounterTextBox(670,475,110,30,"    Fight    ")
    SBMoves = SBEncounterTextBox(670,525,110,30,"     Gun     ")
    SBItems = SBEncounterTextBox(670,575,110,30,"    Items    ")
    SBRun = SBEncounterTextBox(670,625,110,30,  "     Run     ")
   # Gun moves
    GunPowershot = SBEncounterTextBox(670,475,110,30,"Power Shot")
    GunHeal = SBEncounterTextBox(670,525,110,30,"Stimpack")
    GunHealthshot = SBEncounterTextBox(670,575,110,30,"Health Shot")
    GunBack = SBEncounterTextBox(670,625,110,30,"Back")

   # Battle text
    SBAttack = SBEncounterTextBox(0,0,700,100,"You attacked!")
    SBGunPowershot = SBEncounterTextBox(0,0,700,100,"Power Shot!")
    SBGunHeal = SBEncounterTextBox(0,0,700,100,"Stimpack!")
    SBGunHealthshot = SBEncounterTextBox(0,0,700,100,"Health Shot!")
    SBAttacked = SBEncounterTextBox(0,0,700,100,"Enemy attacked!")
    SBEscape = SBEncounterTextBox(0,0,700,100,"You escaped!")
    SBEscapefail = SBEncounterTextBox(0,0,700,100,"Couldn't escape!")
   # Battle logs
    SBBattlelog1 = SBEncounterTextBox(70,485,500,20,"")
    SBBattlelog2 = SBEncounterTextBox(70,505,500,20,"")
    SBBattlelog3 = SBEncounterTextBox(70,525,500,20,"Enemy Encountered!")
    SBBattlelog4 = SBEncounterTextBox(70,545,500,20,"")
    SBBattlelog5 = SBEncounterTextBox(70,565,500,20,"Click Fight for a regular attack")
    SBBattlelog6 = SBEncounterTextBox(70,585,500,20,"Click Gun for special moves")
    SBBattlelog7 = SBEncounterTextBox(70,605,500,20,"Items currently in progress")
    SBBattlelog8 = SBEncounterTextBox(70,625,500,20,"Click Run to attempt to flee, but be quick, you won't have long")
   # Other
    SBLavaWarning = SBEncounterTextBox(350,650,200,30,"I shouldn't get too close to the lava")
    Objectivetext1 = SBEncounterTextBox(350,5,200,30,"Objective: Find and deactivate the alien structures")
    Objectivetext2 = SBEncounterTextBox(350,5,200,30,"Objective: Deactivate the other alien structure")
    Objectivetext3 = SBEncounterTextBox(350,5,200,30,"Objective: Go back to the ship")
#   Enemies
    class SBenemy(pygame.sprite.Sprite):
        def __init__(self, health, attack, x, y, move, radius):
            self.health = health
            self.attack = attack
            self.x = x
            self.y = y
            self.w = 50
            self.h = 75
            self.move = move
            self.radius = radius
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            self.timer = 0
            self.timer2 = 0
            self.alive = True
            self.Your_Turn = True
            self.SBEncountering = False
            self.attackclicked = False
            self.gunclicked = False
            self.itemsclicked = False
            self.runclicked = False
            self.runclickedfailed = False
            self.clicked = ""
            self.enemyattacked = False
            self.escaped = False
            self.direw = 0
            self.dirns = 0
            self.run = 0
            self.running = False

        def draw_enemy(self):
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            if self.alive:
                if self.run >= 20:
                    self.run = 0
                #North...
                if self.dirns == 1:
                    if self.direw == 1:
                        #NorthEast
                        if self.running:
                            if self.run >= 0 and self.run < 5:
                                gameDisplay.blit(ARB1, (self.x,self.y))
                                self.run += 1
                            if self.run >= 5 and self.run < 10:
                                gameDisplay.blit(ARB2, (self.x,self.y))
                                self.run += 1
                            if self.run >= 10 and self.run < 15:
                                gameDisplay.blit(ARB3, (self.x,self.y))
                                self.run += 1
                            if self.run >= 15 and self.run < 20:
                                gameDisplay.blit(ARB2, (self.x,self.y))
                                self.run += 1
                        else:
                            gameDisplay.blit(ARB2, (self.x,self.y))
                    if self.direw == 0:
                        #North
                        if self.running:
                            if self.run >= 0 and self.run < 5:
                                gameDisplay.blit(AB1, (self.x,self.y))
                                self.run += 1
                            if self.run >= 5 and self.run < 10:
                                gameDisplay.blit(AB2, (self.x,self.y))
                                self.run += 1
                            if self.run >= 10 and self.run < 15:
                                gameDisplay.blit(AB3, (self.x,self.y))
                                self.run += 1
                            if self.run >= 15 and self.run < 20:
                                gameDisplay.blit(AB2, (self.x,self.y))
                                self.run += 1
                        else:
                            gameDisplay.blit(AB2, (self.x,self.y))
                    if self.direw == -1:
                        #NorthWest
                        if self.running:
                            if self.run >= 0 and self.run < 5:
                                gameDisplay.blit(ALB1, (self.x,self.y))
                                self.run += 1
                            if self.run >= 5 and self.run < 10:
                                gameDisplay.blit(ALB2, (self.x,self.y))
                                self.run += 1
                            if self.run >= 10 and self.run < 15:
                                gameDisplay.blit(ALB3, (self.x,self.y))
                                self.run += 1
                            if self.run >= 15 and self.run < 20:
                                gameDisplay.blit(ALB2, (self.x,self.y))
                                self.run += 1
                        else:
                            gameDisplay.blit(ALB2, (self.x,self.y))
                #...
                if self.dirns == 0:
                    if self.direw == 1:
                        #East
                        if self.running:
                            if self.run >= 0 and self.run < 5:
                                gameDisplay.blit(AR1, (self.x,self.y))
                                self.run += 1
                            if self.run >= 5 and self.run < 10:
                                gameDisplay.blit(AR2, (self.x,self.y))
                                self.run += 1
                            if self.run >= 10 and self.run < 15:
                                gameDisplay.blit(AR3, (self.x,self.y))
                                self.run += 1
                            if self.run >= 15 and self.run < 20:
                                gameDisplay.blit(AR2, (self.x,self.y))
                                self.run += 1
                        else:
                            gameDisplay.blit(AR0, (self.x,self.y))
                    if self.direw == 0:
                        #X
                        if self.running:
                            if self.run >= 0 and self.run < 5:
                                gameDisplay.blit(AF1, (self.x,self.y))
                                self.run += 1
                            if self.run >= 5 and self.run < 10:
                                gameDisplay.blit(AF2, (self.x,self.y))
                                self.run += 1
                            if self.run >= 10 and self.run < 15:
                                gameDisplay.blit(AF3, (self.x,self.y))
                                self.run += 1
                            if self.run >= 15 and self.run < 20:
                                gameDisplay.blit(AF2, (self.x,self.y))
                                self.run += 1
                        else:
                            gameDisplay.blit(AF0, (self.x,self.y))
                    if self.direw == -1:
                        #West
                        if self.running:
                            if self.run >= 0 and self.run < 5:
                                gameDisplay.blit(AL1, (self.x,self.y))
                                self.run += 1
                            if self.run >= 5 and self.run < 10:
                                gameDisplay.blit(AL2, (self.x,self.y))
                                self.run += 1
                            if self.run >= 10 and self.run < 15:
                                gameDisplay.blit(AL3, (self.x,self.y))
                                self.run += 1
                            if self.run >= 15 and self.run < 20:
                                gameDisplay.blit(AL2, (self.x,self.y))
                                self.run += 1
                        else:
                            gameDisplay.blit(AL0, (self.x,self.y))
                #South...
                if self.dirns == -1:
                    if self.direw == 1:
                        #SouthEast
                        if self.running:
                            if self.run >= 0 and self.run < 5:
                                gameDisplay.blit(ARF1, (self.x,self.y))
                                self.run += 1
                            if self.run >= 5 and self.run < 10:
                                gameDisplay.blit(ARF2, (self.x,self.y))
                                self.run += 1
                            if self.run >= 10 and self.run < 15:
                                gameDisplay.blit(ARF3, (self.x,self.y))
                                self.run += 1
                            if self.run >= 15 and self.run < 20:
                                gameDisplay.blit(ARF2, (self.x,self.y))
                                self.run += 1
                        else:
                            gameDisplay.blit(ARF0, (self.x,self.y))
                    if self.direw == 0:
                        #South
                        if self.running:
                            if self.run >= 0 and self.run < 5:
                                gameDisplay.blit(AF1, (self.x,self.y))
                                self.run += 1
                            if self.run >= 5 and self.run < 10:
                                gameDisplay.blit(AF2, (self.x,self.y))
                                self.run += 1
                            if self.run >= 10 and self.run < 15:
                                gameDisplay.blit(AF3, (self.x,self.y))
                                self.run += 1
                            if self.run >= 15 and self.run < 20:
                                gameDisplay.blit(AF2, (self.x,self.y))
                                self.run += 1
                        else:
                            gameDisplay.blit(AF0, (self.x,self.y))
                    if self.direw == -1:
                        #SouthWest
                        if self.running:
                            if self.run >= 0 and self.run < 5:
                                gameDisplay.blit(ALF1, (self.x,self.y))
                                self.run += 1
                            if self.run >= 5 and self.run < 10:
                                gameDisplay.blit(ALF2, (self.x,self.y))
                                self.run += 1
                            if self.run >= 10 and self.run < 15:
                                gameDisplay.blit(ALF3, (self.x,self.y))
                                self.run += 1
                            if self.run >= 15 and self.run < 20:
                                gameDisplay.blit(ALF2, (self.x,self.y))
                                self.run += 1
                        else:
                            gameDisplay.blit(ALF0, (self.x,self.y))
            else:
                gameDisplay.blit(AlienDead, (self.x,self.y))

        def battlelogupdate(self,text):
            SBBattlelog1.text = SBBattlelog2.text
            SBBattlelog2.text = SBBattlelog3.text
            SBBattlelog3.text = SBBattlelog4.text
            SBBattlelog4.text = SBBattlelog5.text
            SBBattlelog5.text = SBBattlelog6.text
            SBBattlelog6.text = SBBattlelog7.text
            SBBattlelog7.text = SBBattlelog8.text
            SBBattlelog8.text = text

        def Encounter(self):
            if self.escaped:
                if self.timer2 <= FPS:
                    self.timer2 += 1
                if self.timer2 >= FPS:
                    self.escaped = False
                    self.timer2 = 0
        #           Collision
            if self.alive:
                if not self.escaped:
                    if SBMainChar.x >= self.x and SBMainChar.x <= self.x + self.w or SBMainChar.x + SBMainChar.w >= self.x and SBMainChar.x + SBMainChar.w <= self.x + self.w:
                        if SBMainChar.y >= self.y and SBMainChar.y <= self.y + self.h or SBMainChar.y + SBMainChar.h >= self.y and SBMainChar.y + SBMainChar.h <= self.y + self.h:
                            if self.timer <= FPS:
                                SBEncountertext.bigmessage_display()
                                self.timer += 1
                                self.SBEncountering = True
                            if self.timer >= FPS:
                                if self.SBEncountering:
                    #               Drawing the encounter
                                    pygame.draw.rect(gameDisplay, gray, [25, 100, 850, 600]) # Initial box
                                    pygame.draw.rect(gameDisplay, black, [60,150,775,275]) # Enemy visual box
                                    pygame.draw.rect(gameDisplay, black, [60,475,510,180]) # Battle log box
                    #               Battle log text
                                    SBBattlelog1.Battlelogtext()
                                    SBBattlelog2.Battlelogtext()
                                    SBBattlelog3.Battlelogtext()
                                    SBBattlelog4.Battlelogtext()
                                    SBBattlelog5.Battlelogtext()
                                    SBBattlelog6.Battlelogtext()
                                    SBBattlelog7.Battlelogtext()
                                    SBBattlelog8.Battlelogtext()
                                    (SBEncounterTextBox(425,105,50,30,"Enemy Health: " + str(self.health))).EncounterText()
                                    (SBEncounterTextBox(550,700,50,30,"Gun energy: " + str(SBMainChar.stam))).EncounterText()
                    #               When does the combat end
                                    if self.health <= 0:
                                        self.die()
                                    if not self.alive:
                                            self.SBEncountering = False
                                            SBMainChar.kills += 1
                                            SBMainChar.stam = 100
                                            self.timer = 0
                                            self.battlelogupdate("Enemy encountered!")
                                            self.Your_Turn = True                                     
                #                   Your turn
                                    if self.Your_Turn:
                                        if self.timer2 == 0:
                    #                       Click the things
                                            if SBFight.addbox().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                                self.attackclicked = True
                                            if SBMoves.addbox().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                                self.gunclicked = True
                                            if SBItems.addbox().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                                self.itemsclicked = True
                                            if SBRun.addbox().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                                if random.randint(0,100) < 75:
                                                    self.runclicked = True
                                                else:
                                                    self.runclickedfailed = True
                    #                       Do the things
                                        if not self.gunclicked and not self.itemsclicked:
                                            SBFight.addbox()
                                            SBFight.EncounterText()
                                            SBMoves.addbox()
                                            SBMoves.EncounterText()
                                            SBItems.addbox()
                                            SBItems.EncounterText()
                                            SBRun.addbox()
                                            SBRun.EncounterText()
                                        if self.attackclicked:
                                            if self.timer2 <= FPS:
                                                SBAttack.bigmessage_display()
                                                self.timer2 += 1
                                            if self.timer2 > FPS:
                                                self.attacked(1,0,0)
                                                self.Your_Turn = False
                                                self.attackclicked = False
                                                self.timer2 = 0
                                        if self.gunclicked:
                                            if self.timer2 == 1:
                                                self.battlelogupdate("")
                                            if self.timer2 == 4:
                                                self.battlelogupdate("Powershot deals 1.5 x dmg and costs 20 gun energy")
                                            if self.timer2 == 7:
                                                self.battlelogupdate("Healing heals you for 100 dmg at the cost of 25 gun energy")
                                            if self.timer2 == 10:
                                                self.battlelogupdate("Health shot will dmg you, but deal double dmg to the enemy")
                                            if self.timer2 == 13:
                                                self.battlelogupdate("(dmg to self can't crit)")
                                            if self.timer2 == 16:
                                                self.battlelogupdate("Click back to go back")
                                            if self.timer2 <= 16:
                                                self.timer2 += 1
                                                SBFight.addbox()
                                                SBMoves.addbox()
                                                SBItems.addbox()
                                                SBRun.addbox()
                                            if self.timer2 > 16:
                                                if SBFight.addbox().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                                    self.clicked = "Powershot"
                                                if SBMoves.addbox().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                                    self.clicked = "Healing"
                                                if SBItems.addbox().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                                    self.clicked = "Health shot"
                                                if SBRun.addbox().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                                    self.clicked = "Back"
                                                GunPowershot.EncounterText()
                                                GunHeal.EncounterText()
                                                GunHealthshot.EncounterText()
                                                GunBack.EncounterText()
                                        if self.clicked == "Powershot":
                                            if SBMainChar.stam >= 20:
                                                if self.timer2 <= 45:
                                                    SBGunPowershot.bigmessage_display()
                                                    self.timer2 += 1
                                                if self.timer2 > 45:
                                                    self.attacked(1.5, 20, 0)
                                                    self.Your_Turn = False
                                                    self.gunclicked = False
                                                    self.clicked = ""
                                                    self.timer2 = 0
                                            else:
                                                self.battlelogupdate("Not enough energy ( 20 gun energy )")
                                                self.clicked = ""
                                                time.sleep(0.2)
                                        if self.clicked == "Healing":
                                            if SBMainChar.stam >= 25:
                                                if self.timer2 <= 45:
                                                    SBGunHeal.bigmessage_display()
                                                    self.timer2 += 1
                                                if self.timer2 > 45:
                                                    self.attacked(0,25,100)
                                                    self.Your_Turn = False
                                                    self.gunclicked = False
                                                    self.clicked = ""
                                                    self.timer2 = 0
                                            else:
                                                self.battlelogupdate("Not enough energy! ( 25 energy )")
                                                self.clicked = ""
                                                time.sleep(0.2)
                                        if self.clicked == "Health shot":
                                            if self.timer2 <= 45:
                                                SBGunHealthshot.bigmessage_display()
                                                self.timer2 += 1
                                            if self.timer2 > 45:
                                                self.attacked(2,0,-(SBMainChar.attack))
                                                self.Your_Turn = False
                                                self.gunclicked = False
                                                self.clicked = ""
                                                self.timer2 = 0
                                        if self.clicked == "Back":
                                            self.gunclicked = False
                                            if self.timer2 == 17 and SBBattlelog1.text != "":
                                                self.battlelogupdate("")
                                            if self.timer2 == 20:
                                                self.battlelogupdate("Click Fight for a regular attack")
                                            if self.timer2 == 23:
                                                self.battlelogupdate("Click Gun for special moves")
                                            if self.timer2 == 26:
                                                self.battlelogupdate("Items currently in progress")
                                            if self.timer2 == 29:
                                                self.battlelogupdate("Click Run to attempt to flee, but be quick, you won't have long")
                                            if self.timer2 <= 30:
                                                self.timer2 += 1
                                            if self.timer2 > 30:
                                                self.timer2 = 0
                                                self.clicked = ""
                                        if self.itemsclicked:
                                            self.itemsclicked = False
                                        if self.runclicked:
                                            if self.timer2 <= FPS:
                                                SBEscape.bigmessage_display()
                                                self.timer2 += 1
                                            if self.timer2 > FPS:
                                                self.SBEncountering = False
                                                self.runclicked = False
                                                self.escaped = True
                                                self.timer = 0
                                                self.timer2 = 0
                                                time.sleep(1)
                                                self.battlelogupdate("You escaped! (75%)")
                                        if self.runclickedfailed:
                                            if self.timer2 <= FPS:
                                                SBEscapefail.bigmessage_display()
                                                self.timer2 += 1
                                            if self.timer2 > FPS:
                                                self.Your_Turn = False
                                                self.runclickedfailed = False
                                                self.timer2 = 0
                                                time.sleep(1)
                                                self.battlelogupdate("You failed to escape (75%)")
                #                   Enemy's turn
                                    if not self.Your_Turn:
                                        if self.timer2 <= FPS:
                                            SBAttacked.bigmessage_display()
                                            self.timer2 += 1
                                        if self.timer2 >= FPS:
                                            self.attacking()
                                            self.Your_Turn = True
                                            self.timer2 = 0

        def attacked(self, dmgmult, stam, heal):
            self.battlelogupdate("")
            if random.randint(0,100) > 90:
                dmgmult = dmgmult * 2
                heal = heal * 2
                if self.clicked == "Healing":
                    self.battlelogupdate("Critical shot! Double healing")
                else:
                    self.battlelogupdate("Critical shot! Double damage")
            damage = SBMainChar.attack * dmgmult
            if self.clicked == "Healing":
                self.battlelogupdate("You healed " + str(heal) + " damage")
                SBMainChar.stam -= stam
                SBMainChar.health += heal
            else:
                self.battlelogupdate("You attacked for " + str(damage) + " damage")
                self.health -= damage
                SBMainChar.stam -= stam
                SBMainChar.health += heal
        
        def attacking(self):
            dmg = self.attack
            if random.randint(0,100) > 90:
                dmg = dmg * 2
                self.battlelogupdate("Critical hit! Double damage")
            self.battlelogupdate("The enemy attacked you for " + str(dmg) + " damage")
            SBMainChar.health -= dmg
        
        def die(self):
            self.alive = False

        def Encountering(self):
            return self.SBEncountering
        
    SBenemy1 = SBenemy(100, 10, -885, 1850, 9, 350) #At obj 2
    SBenemy2 = SBenemy(150, 15, 1185, 1553, 9, 400) #at obj 1, front
    SBenemy3 = SBenemy(200, 20, 1245, 1793, 5, 350) #at obj 1, behind
    SBenemy4 = SBenemy(100, 10, 375, 1763, 5, 1000) #big radius, slow spd. Big robot sprite
    SBenemy5 = SBenemy(150, 15, 1315, 463, 7, 200) #rando
    SBenemy6 = SBenemy(100, 20, -615, 553, 9, 300) #rando
    SBenemy7 = SBenemy(500, 20, 433, 500, 0, 0) #stationairy, appears after both objectives are found. Sprite with no movement.
    
    Aliens = [SBenemy1,SBenemy2,SBenemy3,SBenemy4,SBenemy5,SBenemy6,SBenemy7]
#   Objectives
    class objective(pygame.sprite.Sprite):
        def __init__(self, x, y, w, h ):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.touched = False
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        
        def draw_obj(self):
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            if not self.touched:
                gameDisplay.blit(Obj_act, (self.x,self.y))
            if self.touched:
                gameDisplay.blit(Obj_inact, (self.x,self.y + 5))
            if pygame.sprite.collide_rect(self, SBMainChar):
                self.touched = True
            
    Objective1 = objective(1235, 1653, 50, 30)
    Objective2 = objective(-825, 1813, 50, 30)
#   Objects
    class Object(pygame.sprite.Sprite):
        def __init__(self, x, y, w, h, image):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            self.image = image
            self.healing = False
            self.timer = 0
            self.tims = 0
            self.dir = 0
        
        def draw_Object(self):
            if not self.healing:
                gameDisplay.blit(self.image, (self.x,self.y))
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        def Healing(self):
            if self.healing:
                if self.timer >= 0 and self.timer < 3:
                    gameDisplay.blit(Heal1img, (self.x,self.y))
                    self.timer += 1
                if self.timer >= 3 and self.timer < 6:
                    gameDisplay.blit(Heal2img, (self.x,self.y))
                    self.timer += 1
                if self.timer >= 6 and self.timer < 9:
                    gameDisplay.blit(Heal3img, (self.x,self.y))
                    self.timer += 1
                if self.timer >= 9 and self.timer < 12:
                    gameDisplay.blit(Heal4img, (self.x,self.y))
                    self.timer += 1
                if self.timer >= 12 and self.timer < 15:
                    gameDisplay.blit(Heal5img, (self.x,self.y))
                    self.timer += 1
                if self.timer >= 15 and self.timer < 18:
                    gameDisplay.blit(Heal6img, (self.x,self.y))
                    self.timer += 1
                if self.timer >= 18 and self.timer < 21:
                    gameDisplay.blit(Heal7img, (self.x,self.y))
                    self.timer += 1
                if self.timer >= 21 and self.timer < 24:
                    gameDisplay.blit(Heal8img, (self.x,self.y))
                    self.timer += 1
                if self.timer >= 24 and self.timer < 27:
                    gameDisplay.blit(Heal9img, (self.x,self.y))
                    self.timer += 1
                if self.timer >= 27 and self.timer < 30:
                    gameDisplay.blit(Heal10img, (self.x,self.y))
                    self.timer += 1
                if self.timer >= 30 and self.timer < 33:
                    gameDisplay.blit(Heal11img, (self.x,self.y))
                    self.timer += 1
                if self.timer == 33:
                    self.timer = 0

    Background = Object(-1015, -207, 2700, 2385, Backgroundimg)
    Mountains = Object(-1015, -207, 2700, 357, None)
    LavaLake = Object(-1015, 1930, 2700, 250, None)
    Healing_ship = Object(400,425, 100, 100, Healsimg)
    Quit_Button = Object(5, 5, 67, 65, Quit_Butt)
#   Classless defs
    def moveworld(direction, speed):
        if direction == "right":
            SBMainChar.x -= speed
            Background.x -= speed 
            Mountains.x -= speed
            LavaLake.x -= speed
            Healing_ship.x -= speed
            Objective1.x -= speed
            Objective2.x -= speed
            for alien in Aliens:
                alien.x -= speed

        if direction == "left":
            SBMainChar.x += speed
            Background.x += speed
            Mountains.x += speed
            LavaLake.x += speed
            Healing_ship.x += speed
            Objective1.x += speed
            Objective2.x += speed
            for alien in Aliens:
                alien.x += speed

        if direction == "up":
            SBMainChar.y += speed
            Background.y += speed
            Mountains.y += speed
            LavaLake.y += speed
            Healing_ship.y += speed
            Objective1.y += speed
            Objective2.y += speed
            for alien in Aliens:
                alien.y += speed

        if direction == "down":
            SBMainChar.y -= speed
            Background.y -= speed
            Mountains.y -= speed
            LavaLake.y -= speed
            Healing_ship.y -= speed
            Objective1.y -= speed
            Objective2.y -= speed
            for alien in Aliens:
                alien.y -= speed
#   Game loop!
    def SBgame_loop():
        
        SpaceBound_Exit = False
        counter = 0
        times = 0
        Obj_Cleared = False
        while not SpaceBound_Exit:
        #   Other things 1
            score = SBMainChar.scoring()
            if SBenemy1.Encountering() or SBenemy2.Encountering() or SBenemy3.Encountering() or SBenemy4.Encountering() or SBenemy5.Encountering() or SBenemy6.Encountering() or SBenemy7.Encountering():
                InEncounter = True
            else:
                InEncounter = False
            if not InEncounter:
                if pygame.sprite.collide_rect(Healing_ship, SBMainChar):
                    if SBMainChar.health < 500:
                        SBMainChar.health += 1
                        Healing_ship.healing = True
                    else:
                        Healing_ship.healing = False
                else:
                    Healing_ship.healing = False
        #   When the game is over        
            pygame.event.pump()
            if pygame.event.peek(pygame.QUIT): 
                game_over.start(score)
                
            if Objective1.touched and Objective2.touched and not SBenemy7.alive:
                score += int(10000000/counter)
                game_over.start(score)

            if SBMainChar.health <= 0:
                game_over.start(score)

            if pygame.mouse.get_pos()[0] >= 5 and pygame.mouse.get_pos()[1] >= 5:
                if pygame.mouse.get_pos()[0] <= 72 and pygame.mouse.get_pos()[1] <= 70:
                    if pygame.mouse.get_pressed()[0]:
                        game_over.start(score)

            if not InEncounter:
        #   Character movement
            #   Move left
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    SBleft = -10 
                    if SBMainChar.x < 0:
                        SBleft = 0 
                    if SBMainChar.x < SBMainChar.w + 300:
                        if Background.x < -5:
                            moveworld("left", 10)
                    SBMainChar.x += SBleft
                    SBMainChar.direction = "left"
                else:
                    SBleft = 0
            #   Move right
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    SBright = 10 
                    if SBMainChar.x > display_width - SBMainChar.w:
                        SBright = 0
                    if SBMainChar.x > display_width - SBMainChar.w - 300:
                        if Background.x > -1795:
                            moveworld("right", 10)
                    SBMainChar.x += SBright
                    SBMainChar.direction = "right"
                else:
                    SBright = 0
            #   Move up
                if pygame.key.get_pressed()[pygame.K_UP]:
                    SBup = -10 
                    if SBMainChar.y < 0:
                        SBup = 0
                    if SBMainChar.y <= Mountains.y + Mountains.h :
                        SBup = 0
                    if SBMainChar.y < SBMainChar.h + 300:
                        if Background.y < -10:
                            moveworld("up", 10)
                    SBMainChar.y += SBup
                else:
                    SBup = 0
            #   Move Down
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    SBdown = 10 
                    if SBMainChar.y > display_height - SBMainChar.h:
                        SBdown = 0
                    if SBMainChar.y + SBMainChar.h >= LavaLake.y:
                        SBdown = 0
                    if SBMainChar.y > display_height - SBMainChar.h - 300:
                        if Background.y > -1480:
                            moveworld("down", 10)
                    SBMainChar.y += SBdown
                else: 
                    SBdown = 0
            #   Are you walking?
                if SBup != 0 or SBdown != 0 or SBright != 0 or SBleft != 0:
                    SBMainChar.running = True
                else:
                    SBMainChar.running = False
            #   Enemy Movement
                for alien in Aliens:
                    if alien.alive:
                        if pygame.sprite.collide_circle(alien, SBMainChar):
                        #   Right
                            if alien.x < SBMainChar.x:
                                if SBMainChar.x - alien.x < alien.move:
                                    movex = SBMainChar.x - alien.x
                                else:
                                    movex = alien.move
                        #   Left
                            if alien.x > SBMainChar.x:
                                if alien.x - SBMainChar.x < alien.move:
                                    movex = SBMainChar.x - alien.x
                                else:
                                    movex = -alien.move
                        #   Down
                            if alien.y < SBMainChar.y:
                                if SBMainChar.y - alien.y < alien.move:
                                    movey = SBMainChar.y - alien.y
                                else:
                                    movey = alien.move
                        #   Up
                            if alien.y > SBMainChar.y:
                                if alien.y - SBMainChar.y < alien.move:
                                    movey = SBMainChar.y - alien.y
                                else:
                                    movey = -alien.move
                        else:
                            movex = 0
                            movey = 0
                    #   Directions
                        if movex > 0:
                            alien.direw = 1
                        if movex < 0:
                            alien.direw = -1
                        if movey > 0:
                            alien.dirns = -1
                        if movey < 0:
                            alien.dirns = 1
                        if movey == 0 and movex == 0:
                            alien.running = False
                        else: 
                            alien.running = True
                    alien.x += movex
                    alien.y += movey  
        #   Create the world
            CharacterHealth = SBEncounterTextBox(425,700,50,30, "Health: " + str(SBMainChar.health))
            Score = SBEncounterTextBox(800,700,100,30,"Score: " + str(int(SBMainChar.scoring())))
            Timer = SBEncounterTextBox(800,5,100,30,"Time: "+str(int(counter/30)))
            ObjClear = SBEncounterTextBox(350, SBMainChar.y + 80,100,30,"You deactivated the structure. You feel your power growing stronger...")
            gameDisplay.fill(black)   
            Background.draw_Object()
        #   Draw the things 
            CharacterHealth.EncounterText()
            Score.EncounterText()
            Timer.EncounterText()
            if Objective1.touched and Objective2.touched:
                Objectivetext3.EncounterText()
                Obj_Cleared = True
                SBMainChar.attack = 50
                if times <= 60:
                    ObjClear.EncounterText()
                    times += 1
            elif Objective1.touched or Objective2.touched:
                Objectivetext2.EncounterText()
                SBMainChar.attack = 25
                if times <= 30:
                    ObjClear.EncounterText()
                    times += 1
            else:
                Objectivetext1.EncounterText()
            if SBMainChar.y + SBMainChar.h >= LavaLake.y:
                SBLavaWarning.EncounterText()
            Quit_Button.draw_Object()
            Healing_ship.draw_Object()
            Objective1.draw_obj() 
            Objective2.draw_obj()
            for alien in Aliens:
                if alien != SBenemy7:
                    alien.draw_enemy()
                if alien == SBenemy7:
                    if Obj_Cleared:
                        alien.draw_enemy()
            SBMainChar.draw_char()
        #   Allow things to happen
            for alien in Aliens:
                if alien != SBenemy7:
                    alien.Encounter()
                elif Obj_Cleared:
                    alien.Encounter()
            Healing_ship.Healing()
            SBMainChar.scoring()
        #   Other things 2
            counter += 1
            pygame.display.update()
            clock.tick(FPS)
#   Other things!
    SBgame_loop()
    main()