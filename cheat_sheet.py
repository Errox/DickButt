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
            astrodoge.start_astrodoge()          
        elif game_id == 2:
            spacestrike.start_spacestrike()
        elif game_id == 3:
            SpaceBound.start_SpaceBound()
        elif game_id == 5:
            Stranded.start_Stranded()
        elif game_id == 4:
            sumo_smash.start_sumo_smash()


    #initializing pygame's mixer
    # pygame.mixer.init()
    # pygame.mixer.music.load("resource/music/main_menu/main_menu.ogg")
    # pygame.mixer.music.play(-1)
 
    #initiate a image loader
    #beginning of the main loop
    main_loop = True
    

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
                introduction_id(game_id)

        pygame.display.flip()
 
    pygame.quit()
    quit()