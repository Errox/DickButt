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
    import error_screen
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
    pygame.display.set_caption("Look at the controls")
    font = pygame.font.Font('resource/fonts/Arcadepix.ttf', 40)
    clock = pygame.time.Clock()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
    define_location = "main_menu"

    #get the error screens ready when on release
    def introduction_id_bleeding_edge(game_id):
        if game_id == 1:
            try:
                astrodoge.start_astrodoge()
                pass
            except Exception as e:
                print(e)
                error_screen.start(e, game_id)    
                pass            
        elif game_id == 2:
            try:
                spacestrike.start_spacestrike()
                pass
            except Exception as e:
                error_screen.start(e, game_id)                
                pass
        elif game_id == 3:
            try:
                SpaceBound.start_SpaceBound()
                pass
            except Exception as e:
                error_screen.start(e, game_id)                
                pass            
        elif game_id == 4:
            try:
                sumo_smash.start_sumo_smash()
                pass
            except Exception as e:
                error_screen.start(e, game_id)                
                pass
        elif game_id == 5:
            try:
                Stranded.start_Stranded()
                pass
            except Exception as e:
                error_screen.start(e, game_id)                
                pass
        
    #without the error screens
    def introduction_id(game_id):
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
        
 
    #initiate a image loader
    #beginning of the main loop
    main_loop = True
    
    #define the game_id where it's been loaded
    if game_id == 1:
        background = pygame.image.load('resource/images/cheat_sheets/Astrododge_cs.png').convert()
        background_rect = background.get_rect()
    elif game_id == 2:
        background = pygame.image.load('resource/images/cheat_sheets/SpaceStrike_cs.png').convert()
        background_rect = background.get_rect()
    elif game_id == 3:
        background = pygame.image.load('resource/images/cheat_sheets/Spacebound_cs.png').convert()
        background_rect = background.get_rect()
    elif game_id == 4:
        background = pygame.image.load('resource/images/cheat_sheets/Invasion_cs.png').convert()
        background_rect = background.get_rect()
    elif game_id == 5: 
        background = pygame.image.load('resource/images/cheat_sheets/Stranded_cs.png').convert()
        background_rect = background.get_rect()

    #main loop of the cheat_sheet
    while main_loop:
    
        #reset the screen and set screen image's
        screen.fill(BLACK)

        screen.blit(background, background_rect)

        clock.tick(FPS)
        #check events
        for evento in pygame.event.get():
            #define event's of quiting the game.
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                introduction_id_bleeding_edge(game_id)

        pygame.display.flip()
 
    pygame.quit()
    quit()