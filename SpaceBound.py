def start_SpaceBound():
#   imports!        
    import pygame
    import menu
    import time
    import random
    import pygame.locals
    pygame.init()
#   things!
    FPS = 30
    display_width = 900 
    display_height = 900
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('SpaceBound')
    Backgroundimg = pygame.image.load('resource/images/SpaceBound/Background_SpaceBound.gif')
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
        def __init__(self,health,attack,x,y,w,h):
            self.health = health
            self.attack = attack
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            self.kills = 0
            self.count = 0

        def draw_char(self):
            pygame.draw.rect(gameDisplay, green, [self.x,self.y,self.w,self.h])
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        def scoring(self):
            scores = 100 * self.kills + self.count
            return scores

    SBMainChar = SBMainCharacter(5000, 500, 425, 410, 50, 75) #temporarily hightened
#   Texts
    class SBEncounterTextBox(object):
        def __init__(self, x, y, w, h, text):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.text = text

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

        
        def bigmessage_display(self):
            Encounterstart = False
            font = pygame.font.Font('resource/fonts/ka1.ttf', 65)
            TextSurf = font.render(self.text, True, white)
            text_rect = TextSurf.get_rect()
            text_rect.center = ((display_width * 0.5), (display_height * 0.5))
            gameDisplay.blit(TextSurf, text_rect)

    SBEncountertext = SBEncounterTextBox(0,0,700,100,"Encounter!")
    SBFight = SBEncounterTextBox(670,475,110,30,"    Fight    ")
    SBMoves = SBEncounterTextBox(670,525,110,30,"     Gun     ")
    SBItems = SBEncounterTextBox(670,575,110,30,"    Items    ")
    SBRun = SBEncounterTextBox(670,625,110,30,  "     Run     ")
    SBAttack = SBEncounterTextBox(0,0,700,100,"You attacked!")
    SBAttacked = SBEncounterTextBox(0,0,700,100,"Enemy attacked!")
    SBEscape = SBEncounterTextBox(0,0,700,100,"You escaped!")
    SBEscapefail = SBEncounterTextBox(0,0,700,100,"Couldn't escape!")
    SBBattlelog1 = SBEncounterTextBox(70,485,500,20,"")
    SBBattlelog2 = SBEncounterTextBox(70,505,500,20,"")
    SBBattlelog3 = SBEncounterTextBox(70,525,500,20,"")
    SBBattlelog4 = SBEncounterTextBox(70,545,500,20,"")
    SBBattlelog5 = SBEncounterTextBox(70,565,500,20,"")
    SBBattlelog6 = SBEncounterTextBox(70,585,500,20,"")
    SBBattlelog7 = SBEncounterTextBox(70,605,500,20,"")
    SBBattlelog8 = SBEncounterTextBox(70,625,500,20,"Enemy encountered!")
    SBLavaWarning = SBEncounterTextBox(350,650,200,30,"I shouldn't get too close to the lava")
#   Enemies
    class SBenemy(pygame.sprite.Sprite):
        def __init__(self, health, attack, x, y, w, h, move, radius):
            self.health = health
            self.attack = attack
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.move = move
            self.radius = radius
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            self.timer = 0
            self.timer2 = 0
            self.alive = True
            self.Your_Turn = True
            self.SBEncountering = False
            self.attackclicked = False
            self.runclicked = False
            self.runclickedfailed = False
            self.enemyattacked = False
            self.escaped = False

        def draw_enemy(self):
            if self.alive:
                pygame.draw.rect(gameDisplay, red, [self.x,self.y,self.w,self.h])
                self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

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
            if not self.escaped:
                if SBMainChar.x > self.x and SBMainChar.x < self.x + self.w or SBMainChar.x + SBMainChar.w > self.x and SBMainChar.x + SBMainChar.w < self.x + self.w:
                    if SBMainChar.y > self.y and SBMainChar.y < self.y + self.h or SBMainChar.y + SBMainChar.h > self.y and SBMainChar.y + SBMainChar.h < self.y + self.h:
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
                    #           Battle log text
                                SBBattlelog1.Battlelogtext()
                                SBBattlelog2.Battlelogtext()
                                SBBattlelog3.Battlelogtext()
                                SBBattlelog4.Battlelogtext()
                                SBBattlelog5.Battlelogtext()
                                SBBattlelog6.Battlelogtext()
                                SBBattlelog7.Battlelogtext()
                                SBBattlelog8.Battlelogtext()
                                (SBEncounterTextBox(425,105,50,30,"Enemy Health: " + str(self.health))).EncounterText()#enemy health
                #                       When does the combat end
                                if self.health <= 0:
                                    self.SBEncountering = False
                                    self.timer = 0
                                    self.battlelogupdate("Enemy encountered!")
                                    self.Your_Turn = True
                                if SBMainChar.health <= 0:
                                    SpaceBound_Exit = True
            #                   Your turn
                                if self.Your_Turn:
                                    if self.timer2 == 0:
                #                           Create the things
                                        SBFight.addbox()
                                        SBMoves.addbox()
                                        SBItems.addbox()
                                        SBRun.addbox()
                                        SBFight.EncounterText()
                                        SBMoves.EncounterText()
                                        SBItems.EncounterText()
                                        SBRun.EncounterText()
                #                           Click the things
                                        if SBFight.EncounterText().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                            self.attackclicked = True
                                        if SBMoves.EncounterText().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                            print("WIP")
                                            self.Your_Turn = False
                                        if SBItems.EncounterText().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                            print("WIP")
                                            self.Your_Turn = False
                                        if SBRun.EncounterText().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                            if random.randint(0,100) < 75:
                                                self.runclicked = True
                                            else:
                                                self.runclickedfailed = True
                #                       Do the things
                                    if self.attackclicked:
                                        if self.timer2 <= FPS:
                                            SBAttack.bigmessage_display()
                                            self.timer2 += 1
                                        if self.timer2 > FPS:
                                            self.attacked()
                                            self.Your_Turn = False
                                            if not self.alive:
                                                self.SBEncountering = False
                                                SBMainChar.kills += 1
                                            self.attackclicked = False
                                            self.timer2 = 0
                                            time.sleep(1)
                                            self.battlelogupdate("You attacked for " + str(SBMainChar.attack) + " damage")
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
                                        time.sleep(1)
                                        self.battlelogupdate("The enemy attacked you for " + str(self.attack) + " damage")

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
        
    SBenemy1 = SBenemy(100, 10, -885, 1850, 50, 75, 10, 250) #At obj 2
    SBenemy2 = SBenemy(150, 15, 1185, 1553, 50, 75, 5, 300) #at obj 1, front
    SBenemy3 = SBenemy(200, 20, 1245, 1793, 50, 75, 5, 250) #at obj 1, behind
    SBenemy4 = SBenemy(100, 10, 375, 1763, 50, 75, 20, 1000) #big radius, slow spd
    SBenemy5 = SBenemy(150, 15, 1315, 463, 50, 75, 7, 300) #rando
    SBenemy6 = SBenemy(100, 20, -615, 553, 50, 75, 10, 250) #rando
    SBenemy7 = SBenemy(500, 10, 285, 418, 50, 75, 0, 0) #stationairy, appears after both objectives are found

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
            pygame.draw.rect(gameDisplay, blue, [self.x,self.y,self.w,self.h])
            if pygame.sprite.collide_rect(self, SBMainChar):
                self.touched = True
            
    Objective1 = objective(1235, 1653, 50, 50)
    Objective2 = objective(-825, 1813, 50, 50)

#   Objects
    class Object(pygame.sprite.Sprite):
        def __init__(self, x, y, w, h, image):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
            self.image = image
        
        def draw_Object(self):
            gameDisplay.blit(self.image, (self.x,self.y))


    Background = Object(-1015, -207, 2700, 2385, Backgroundimg)
    Mountains = Object(-1015, -207, 2700, 357, None)
    LavaLake = Object(-1015, 1930, 2700, 250, None)
        
#   Classless defs
    def moveworld(direction, speed):
        if direction == "right":
            SBMainChar.x -= speed
            Background.x -= speed 
            Mountains.x -= speed
            LavaLake.x -= speed
            Objective1.x -= speed
            Objective2.x -= speed
            SBenemy1.x -= speed
            SBenemy2.x -= speed
            SBenemy3.x -= speed
            SBenemy4.x -= speed
            SBenemy5.x -= speed
            SBenemy6.x -= speed
            SBenemy7.x -= speed

        if direction == "left":
            SBMainChar.x += speed
            Background.x += speed
            Mountains.x += speed
            LavaLake.x += speed
            Objective1.x += speed
            Objective2.x += speed
            SBenemy1.x += speed
            SBenemy2.x += speed
            SBenemy3.x += speed
            SBenemy4.x += speed
            SBenemy5.x += speed
            SBenemy6.x += speed
            SBenemy7.x += speed

        if direction == "up":
            SBMainChar.y += speed
            Background.y += speed
            Mountains.y += speed
            LavaLake.y += speed
            Objective1.y += speed
            Objective1.y += speed
            SBenemy1.y += speed
            SBenemy2.y += speed
            SBenemy3.y += speed
            SBenemy4.y += speed
            SBenemy5.y += speed
            SBenemy6.y += speed
            SBenemy7.y += speed

        if direction == "down":
            SBMainChar.y -= speed
            Background.y -= speed
            Mountains.y -= speed
            LavaLake.y -= speed
            Objective1.y -= speed
            Objective1.y -= speed
            SBenemy1.y -= speed
            SBenemy2.y -= speed
            SBenemy3.y -= speed
            SBenemy4.y -= speed
            SBenemy5.y -= speed
            SBenemy6.y -= speed
            SBenemy7.y -= speed

#   Game loop!
    def SBgame_loop():
        
        SpaceBound_Exit = False
        counter = 0
        while not SpaceBound_Exit:
            if SBenemy1.Encountering() or SBenemy2.Encountering() or SBenemy3.Encountering() or SBenemy4.Encountering() or SBenemy5.Encountering() or SBenemy6.Encountering() or SBenemy7.Encountering():
                InEncounter = True
            else:
                InEncounter = False
        #   When the game is over        
            pygame.event.pump()
            if pygame.event.peek(pygame.QUIT): 
                print("Clicked X")
                SpaceBound_Exit = True
                
            if Objective1.touched and Objective2.touched:
                SBMainChar.count += 10000000/(1000 + counter)
                Score.bigmessage_display()
                time.sleep(1)
                SpaceBound_Exit = True
            if not InEncounter:
        #   Character movement
            #   Move left
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    SBleft = -10 
                    if SBMainChar.x < 0:
                        SBleft = 0 
                    SBMainChar.x += SBleft
                    if SBMainChar.x < SBMainChar.w + 300:
                        if Background.x < -5:
                            moveworld("left", 10)
            #   Move right
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    SBright = 10 
                    if SBMainChar.x > display_width - SBMainChar.w:
                        SBright = 0
                    if SBMainChar.x > display_width - SBMainChar.w - 300:
                        if Background.x > -1795:
                            moveworld("right", 10)
                    SBMainChar.x += SBright
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

            #   Enemy Movement
                if SBenemy1.alive:
                    if pygame.sprite.collide_circle(SBenemy1, SBMainChar):
                        if SBenemy1.x < SBMainChar.x:
                            movex1 = SBenemy1.move
                        if SBenemy1.x > SBMainChar.x:
                            movex1 = -SBenemy1.move
                        if SBenemy1.y < SBMainChar.y:
                            movey1 = SBenemy1.move
                        if SBenemy1.y > SBMainChar.y:
                            movey1 = -SBenemy1.move
                    else:
                        movex1 = 0
                        movey1 = 0
                SBenemy1.x += movex1
                SBenemy1.y += movey1   
                if SBenemy2.alive:
                    if pygame.sprite.collide_circle(SBenemy2, SBMainChar):
                        if SBenemy2.x < SBMainChar.x:
                            movex2 = SBenemy2.move
                        if SBenemy2.x > SBMainChar.x:
                            movex2 = -SBenemy2.move
                        if SBenemy2.y < SBMainChar.y:
                            movey2 = SBenemy2.move
                        if SBenemy2.y > SBMainChar.y:
                            movey2 = -SBenemy2.move
                    else: 
                        movex2 = 0
                        movey2 = 0
                SBenemy2.x += movex2
                SBenemy2.y += movey2
                if SBenemy3.alive:
                    if pygame.sprite.collide_circle(SBenemy3, SBMainChar):
                        if SBenemy3.x < SBMainChar.x:
                            movex3 = SBenemy3.move
                        if SBenemy3.x > SBMainChar.x:
                            movex3 = -SBenemy3.move
                        if SBenemy3.y < SBMainChar.y:
                            movey3 = SBenemy3.move
                        if SBenemy3.y > SBMainChar.y:
                            movey3 = -SBenemy3.move
                    else:
                        movex3 = 0
                        movey3 = 0
                SBenemy3.x += movex3
                SBenemy3.y += movey3
                if SBenemy4.alive:
                    if pygame.sprite.collide_circle(SBenemy4, SBMainChar):
                        if SBenemy4.x < SBMainChar.x:
                            movex4 = SBenemy4.move
                        if SBenemy4.x > SBMainChar.x:
                            movex4 = -SBenemy4.move
                        if SBenemy4.y < SBMainChar.y:
                            movey4 = SBenemy4.move
                        if SBenemy4.y > SBMainChar.y:
                            movey4 = -SBenemy4.move
                    else:
                        movex4 = 0
                        movey4 = 0
                SBenemy4.x += movex4
                SBenemy4.y += movey4
                if SBenemy5.alive:
                    if pygame.sprite.collide_circle(SBenemy5, SBMainChar):
                        if SBenemy5.x < SBMainChar.x:
                            movex5 = SBenemy5.move
                        if SBenemy5.x > SBMainChar.x:
                            movex5 = -SBenemy5.move
                        if SBenemy5.y < SBMainChar.y:
                            movey5 = SBenemy5.move
                        if SBenemy5.y > SBMainChar.y:
                            movey5 = -SBenemy5.move
                    else:
                        movex5 = 0
                        movey5 = 0
                SBenemy5.x += movex5
                SBenemy5.y += movey5
                if SBenemy6.alive:
                    if pygame.sprite.collide_circle(SBenemy6, SBMainChar):
                        if SBenemy6.x < SBMainChar.x:
                            movex6 = SBenemy6.move
                        if SBenemy6.x > SBMainChar.x:
                            movex6 = -SBenemy6.move
                        if SBenemy6.y < SBMainChar.y:
                            movey6 = SBenemy6.move
                        if SBenemy6.y > SBMainChar.y:
                            movey6 = -SBenemy6.move
                    else:
                        movex6 = 0
                        movey6 = 0
                SBenemy6.x += movex6
                SBenemy6.y += movey6
                
        #   Create the world
            CharacterHealth = SBEncounterTextBox(425,700,50,30, "Health: " + str(SBMainChar.health))
            Score = SBEncounterTextBox(800,5,100,30,"Score: " + str(int(SBMainChar.scoring())))
            Timer = SBEncounterTextBox(0,5,100,30,"Time: "+str(int(counter/30)))
            Objectivetext1 = SBEncounterTextBox(350,5,200,30,"Objective: Go to the two blue squares")
            Objectivetext2 = SBEncounterTextBox(350,5,200,30,"Objective: Go to the other blue square")
            Objectivetext3 = SBEncounterTextBox(350,5,200,30,"Objective: Go back to the ship")
            gameDisplay.fill(black)   
            Background.draw_Object()
        #   Draw the things           
            SBMainChar.draw_char()  
            CharacterHealth.EncounterText()
            Score.EncounterText()
            Timer.EncounterText()
            if Objective1.touched and Objective2.touched:
                Objectivetext3.EncounterText()
            elif Objective1.touched or Objective2.touched:
                Objectivetext2.EncounterText()
            else:
                Objectivetext1.EncounterText()
            if SBMainChar.y + SBMainChar.h >= LavaLake.y:
                SBLavaWarning.EncounterText()
            Objective1.draw_obj() 
            Objective2.draw_obj()
            SBenemy1.draw_enemy()
            SBenemy2.draw_enemy()
            SBenemy3.draw_enemy()
            SBenemy4.draw_enemy()
            SBenemy5.draw_enemy()
            SBenemy6.draw_enemy()
            SBenemy7.draw_enemy()
        #   Allow the enemies to fight you
            SBenemy1.Encounter()
            SBenemy2.Encounter()
            SBenemy3.Encounter()
            SBenemy4.Encounter()
            SBenemy5.Encounter()
            SBenemy6.Encounter()
            SBenemy7.Encounter()
        #   Other things
            counter += 1
            pygame.display.update()
            clock.tick(FPS)

#   Other things!
    SBgame_loop()
    pygame.quit()
    quit()