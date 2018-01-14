def start(score, game_id):
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
    import cheat_sheet
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
    pygame.display.set_caption("Welp, you can always try again!")
    font = pygame.font.Font('resource/fonts/Arcadepix.ttf', 40)
    clock = pygame.time.Clock()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
    define_location = "main_menu"
        
    #initializing pygame's mixer
    # pygame.mixer.init()
    # pygame.mixer.music.load("resource/music/main_menu/main_menu.ogg")
    # pygame.mixer.music.play(-1)

    #initiate a image loader
    def load_image(name):
        image = pygame.image.load(name)
        return image
    
    #create a sprite class to animate 
    class animated_select_planet(pygame.sprite.Sprite):
        def __init__(self):
            super(animated_select_planet, self).__init__()
            self.images = []
            self.images.append(load_image('resource/images/game_over/tekst/game_over_1.png'))
            self.images.append(load_image('resource/images/game_over/tekst/game_over_2.png'))
            self.images.append(load_image('resource/images/game_over/tekst/game_over_3.png'))
            self.images.append(load_image('resource/images/game_over/tekst/game_over_4.png'))
            self.images.append(load_image('resource/images/game_over/tekst/game_over_5.png'))
            self.images.append(load_image('resource/images/game_over/tekst/game_over_6.png'))
            self.images.append(load_image('resource/images/game_over/tekst/game_over_7.png'))
            self.index = 0
            self.image = self.images[self.index]
            self.rect = pygame.Rect(25, 130, 250, 80)

        def update(self):
            self.index += 1
            sleep(0.1)
            if self.index >= len(self.images):
                self.index = 0
                count = 0
            self.image = self.images[self.index]

    #start the main menu board.
    def start_game_over():
        #set background
        background = pygame.image.load('resource/images/game_over/game_overbg.png').convert()
        background_rect = background.get_rect()
        screen.blit(background, background_rect)
        buttons_game_over()
    #game over buttons ready
    def buttons_game_over():
        quit_button         = pygame.image.load('resource/images/game_over/button_quit.png').convert()
        retry_button         = pygame.image.load('resource/images/game_over/button_restart.png').convert()
        quit_rect           = quit_button.get_rect()
        retry_rect           = quit_button.get_rect()
        screen.blit(quit_button, (325,550))
        screen.blit(retry_button, (325,470))
    #score text to screen
    def text_score(score, highscore):       
        scoretext = font.render("Your Score ", 1, WHITE)
        score = font.render(" {0}".format(score), 1, WHITE)
        scorehightext = font.render("Your highscore ", 1, WHITE)
        scorehigh = font.render(" {0}".format(highscore), 1, WHITE)
        screen.blit(scoretext, (250, 385))
        screen.blit(score, (250, 415))
        screen.blit(scorehightext, (500, 385))
        screen.blit(scorehigh, (500, 415))



    #beginning of the main loop
    main_loop = True
    soundboard.game_over(score) 
    my_sprite = animated_select_planet()
    my_group = pygame.sprite.Group(my_sprite)
    highscore.save(score, game_id)
    
    while main_loop:
        #reset the screen and set screen image's
        screen.fill(BLACK)
        clock.tick(FPS)
        start_game_over()
        my_group.update()
        my_group.draw(screen)
        highscorer = highscore.read(game_id)
        text_score(score, highscorer)
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
                if pygame.mouse.get_pos()[0] >= 315 and pygame.mouse.get_pos()[1] >= 470:
                    if pygame.mouse.get_pos()[0] <= 593 and pygame.mouse.get_pos()[1] <= 535:
                        cheat_sheet.start(game_id)
                        
    pygame.quit()
    quit()
