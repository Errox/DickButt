def start(game_id):
    #defining every library needed
    import sys
    import pygame
    import os
    import menu
    import astrodoge
    import spacestrike
    import SpaceBound
    import Stranded
    import sumo_smash
    import soundboard
    from time import sleep
 
    #setting variables
    FPS     = 30
    X       = 500
    Y       = 100
    WHITE   = (255, 255, 255)
    BLACK   = (0, 0, 0)
    count_down = False

    pygame.init()
 
    #setting the settings of pygame itself
    screen = pygame.display.set_mode((900,900))
    pygame.display.set_caption("cheat_sheet")
    font = pygame.font.Font('resource/fonts/Arcadepix.ttf', 40)
    clock = pygame.time.Clock()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
    define_location = "main_menu"
        

    def introduction_id(game_id):
        if game_id == 1:
            print('penis1')            
        elif game_id == 2:
            print('penis2')
        elif game_id == 3:
            print('penis3')            
        elif game_id == 4:
            print('penis4')            
        elif game_id == 5: 
            print('penis5')

    def async(counting):
        scoretext = font.render(str(counting), 1,(255,255,255))
        screen.blit(scoretext, (500, 500))     

    #initializing pygame's mixer
    # pygame.mixer.init()
    # pygame.mixer.music.load("resource/music/main_menu/main_menu.ogg")
    # pygame.mixer.music.play(-1)
 
    #initiate a image loader
    background = pygame.image.load('resource/images/astrodoge/backgrounds/basic_star_bg.png').convert()
    background_rect = background.get_rect()
    #beginning of the main loop
    main_loop = True
    
    counting = 3
    while main_loop:
        screen.blit(background, background_rect)
        while count_down == True:
            screen.fill(BLACK)
            screen.blit(background, background_rect)
            clock.tick(FPS)

            #check events
            for evento in pygame.event.get():
                #define event's of quiting the game.
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #printing every event that's happening within the python script.
                print(evento)
                #Catch mouse position and if it's pressed on the button
                            
            pygame.display.flip()
            for count in range(0,3):
                sleep(1)
                print(counting) 
                async(counting)
                counting -= 1
                if counting == 0:
                    if game_id == 1:
                        astrodoge.start_astrodoge()            
                    elif game_id == 2:
                        spacestrike.start_spacestrike()
                    elif game_id == 3:
                        SpaceBound.start_SpaceBound()
                    elif game_id == 4:
                        sumo_smash.start_sumo_smash()
                    elif game_id == 5: 
                        Stranded.start_Stranded()
                    else:
                        quit()
                
 
        while count_down == False:
            #reset the screen and set screen image's
            screen.fill(BLACK)
            introduction_id(game_id)
            screen.blit(background, background_rect)
            clock.tick(FPS)
            #check events
            for evento in pygame.event.get():
                #define event's of quiting the game.
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif evento.type == pygame.KEYDOWN:
                    count_down = True

            pygame.display.flip()
 
    pygame.quit()
    quit()