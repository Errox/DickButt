   
def read(game_id):
    import json
    data = json.load(open('highscores.json'))
    idtje = str(game_id)
    return data[idtje]

def read_all():
    import json    
    data = json.load(open('highscores.json'))
    return data
 
    
def save(score, game_id):
    import json
    import os
    data = json.load(open('highscores.json'))
    idtje = str(game_id)

    if score > data[idtje]:
        id = str(game_id)
        filename = 'highscores.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            data[id] = score # <--- add `id` value.

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

def start():
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
    pygame.display.set_caption("Look at those scores!")
    font = pygame.font.Font('resource/fonts/Arcadepix.ttf', 40)
    clock = pygame.time.Clock()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
        
    soundboard.hall_of_fame()
    
    def text_score():
        data = highscore.read_all()
        astrodogetext = font.render("Astrodoge_score : {0}".format(data['1']), 1, WHITE)
        spacestext = font.render("Spacestrike_score : {0} ".format(data['2']), 1, WHITE)
        spacetext = font.render("Space Bound_score : {0}".format(data['3']), 1, WHITE)
        sumotext = font.render("Invasion_of_the_unknown_score : {0} ".format(data['4']), 1, WHITE)
        strandedtext = font.render("Stranded_score : {0} ".format(data['5']), 1, WHITE)

        screen.blit(astrodogetext, (150, 385))
        screen.blit(spacestext, (150, 415))
        screen.blit(spacetext, (150, 445))
        screen.blit(sumotext, (150, 475))
        screen.blit(strandedtext, (150, 505))
        


    #beginning of the main loop
    main_loop = True 
    init = False
    while main_loop:
        #reset the screen and set screen image's
        clock.tick(FPS)
        if init == False:
            screen.fill(BLACK)
            background = pygame.image.load('resource/images/highscore/highscore.png')
            background_rect = background.get_rect()
            screen.blit(background, background_rect)
            init = True
            text_score()

        quit_button         = pygame.transform.scale(pygame.image.load ('resource/images/select_planet/button_quit_small.png'), (42,40))
        quit_rect           = quit_button.get_rect()
        screen.blit(quit_button, (5,5)) 

        for event in pygame.event.get():
            #define event's of quiting the game.
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 5 and pygame.mouse.get_pos()[1] >= 5:
                    if pygame.mouse.get_pos()[0] <= 155 and pygame.mouse.get_pos()[1] <= 53:
                        menu.start_menu()

        pygame.display.flip()

    pygame.quit()
    quit()
#start()