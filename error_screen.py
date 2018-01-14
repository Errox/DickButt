def start(error, game_id):
    #defining every library needed
    import sys
    import pygame
    import os
    import menu
    import soundboard
    import highscore
    from time import sleep

    #setting variables
    FPS     = 30
    X       = 500
    Y       = 100
    WHITE   = (255, 255, 255)
    BLACK   = (0, 0, 0)

    #setting the settings of pygame itself
    screen = pygame.display.set_mode((900,900))
    pygame.display.set_caption("Heh, Idunno what happened, but something got messed up, My bad!")
    font = pygame.font.Font('resource/fonts/Arcadepix.ttf', 30)
    clock = pygame.time.Clock()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
    soundboard.error_music()
    #start the main menu board.
    def start_game_over():
        #set background
        background = pygame.image.load('resource/images/game_over/game_overbg.png').convert()
        background_rect = background.get_rect()
        screen.blit(background, background_rect)
        buttons_game_over()
    #get buttons
    def buttons_game_over():
        quit_button         = pygame.image.load('resource/images/game_over/button_quit.png').convert()
        quit_rect           = quit_button.get_rect()
        screen.blit(quit_button, (325,550))
    #set error message ready
    def error(error, game_id):
        scorehigh = font.render("error:  {0}".format(error), 1, WHITE)
        screen.blit(scorehigh, (0, 0))
        if game_id == 1:
            game_name = 'Astrododge'
        elif game_id == 2: 
            game_name = 'SpaceStrike'
        elif game_id == 3:
            game_name = 'Space_Bound'
        elif game_id == 5:
            game_name = 'Stranded'
        elif game_id == 4:
            game_name = 'sumo_smash'
        else:
            game_name = 'Unkown'
        
        scorehigh = font.render("Game {0} has crashed ".format(game_name), 1, WHITE)
        screen.blit(scorehigh, (0, 30))

    #beginning of the main loop
    main_loop = True
    
    while main_loop:
        #reset the screen and set screen image's
        screen.fill(BLACK)
        clock.tick(FPS)
        error(error, game_id)
        buttons_game_over()
        pygame.display.flip()

        #check events
        for evento in pygame.event.get():
            #define event's of quiting the game.
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            #printing every event that's happening within the python script.
            print(evento)
            #Catch mouse position and if it's pressed on the button
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 325 and pygame.mouse.get_pos()[1] >= 550:
                    if pygame.mouse.get_pos()[0] <= 593 and pygame.mouse.get_pos()[1] <= 615:
                        menu.start_menu()

    pygame.quit()
    quit()
 
