def start_menu():
    #import all library's 
    import sys
    import pygame
    import os
    import game_over
    import astrodoge 
    import spacestrike
    import soundboard
    from time import sleep
    
    #All global variables are set here
    FPS     = 30
    X       = 500
    Y       = 100
    BLACK   = (0, 0, 0)
    
    #Here we set all window properties
    screen = pygame.display.set_mode((900,900))
    pygame.display.set_caption("Menu")
    clock = pygame.time.Clock()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
    define_location = "main_menu"
        
    #create main_menu sound
    soundboard.main_menu()
    
    #here we define a class to load a image in a multiple way to make it look a little better. We use this def to manupilate the image if needed
    def load_image(name):
        image = pygame.image.load(name)
        return image

    #set the class of a animated text that is used in the scene select_planet

    class animated_select_planet(pygame.sprite.Sprite):
        def __init__(self):
            super(animated_select_planet, self).__init__()
            self.images = []
            self.images.append(load_image('resource/images/select_planet/select_planet_animation/selectplanet_glow_1.png'))
            self.images.append(load_image('resource/images/select_planet/select_planet_animation/selectplanet_glow_2.png'))
            self.images.append(load_image('resource/images/select_planet/select_planet_animation/selectplanet_glow_3.png'))
            self.images.append(load_image('resource/images/select_planet/select_planet_animation/selectplanet_glow_4.png'))
            self.images.append(load_image('resource/images/select_planet/select_planet_animation/selectplanet_glow_5.png'))
            self.images.append(load_image('resource/images/select_planet/select_planet_animation/selectplanet_glow_6.png'))
            self.images.append(load_image('resource/images/select_planet/select_planet_animation/selectplanet_glow_7.png'))
            self.images.append(load_image('resource/images/select_planet/select_planet_animation/selectplanet_glow_8.png'))
            self.images.append(load_image('resource/images/select_planet/select_planet_animation/selectplanet_glow_9.png'))
            self.index = 0
            self.image = self.images[self.index]
            self.rect = pygame.Rect(275, 520, 250, 80)
      
        #here we update the sprite used for the animated text. 
        def update(self):
            self.index += 1
            sleep(0.1)
            if self.index >= len(self.images):
                self.index = 0
                count = 0
            self.image = self.images[self.index]

    # 1 #
    #start the main menu board.
    def start_main_menu():
        #set background
        background = pygame.image.load('resource/images/main_menu/main_menu.png').convert()
        background_rect = background.get_rect()
        screen.blit(background, background_rect)
        pygame.display.set_caption("Main_menu")

    #start the select_planet scene and blit everything to screen
    def start_select_planet():
        #setting up background and title. Then call select_plannet_buttons to load them in after a new scene has been created
        background = pygame.image.load('resource/images/select_planet/select_planet_background.png')
        background_rect = background.get_rect()
        screen.blit(background, background_rect)
        pygame.display.set_caption("Select Planet")
        #get buttons
        my_group.update()
        my_group.draw(screen)
        buttons_select_planet()
    #here we define the button used in the select_planet scene
    def buttons_select_planet():
        quit_button         = pygame.image.load('resource/images/select_planet/button_quit_small.png').convert()
        quit_rect           = quit_button.get_rect()
        screen.blit(quit_button, (5,5))

    #Function to place text on screen. 
    def text(text, x, y):
        #make a text and render it to the given x, y cordinates
        font = pygame.font.Font("resource/fonts/Arcadepix.ttf",30)
        text = font.render(str(text), 1,(255,255,255))
        screen.blit(text, (x, y))

    #Defining some information before we start pygame. 
    main_loop = True
    my_sprite = animated_select_planet()
    my_group = pygame.sprite.Group(my_sprite)

    #start of the main_loop
    while main_loop:
        #reset the screen. and set fps rate
        screen.fill(BLACK)
        clock.tick(FPS)
        #here we check which functions come to make the storyboard functional
        if define_location == "main_menu":
            start_main_menu()
        elif define_location == "select_planet":
            start_select_planet()
        elif define_location == "planet_astrodoge":
            pygame.mixer.music.stop()
            astrodoge.start_astrodoge()
        elif define_location == "planet_spacestrike":
            pygame.mixer.music.stop()
            spacestrike.start_spacestrike()
        else:
            print('under construction')

        #every event is logged here with all actions 
        for evento in pygame.event.get():
            #define event's of quiting the game.
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    game_over.start(9999999999999999)    
                if evento.key == pygame.K_DOWN:
                    soundboard.pause()   
            #printing every event that's happening within the python script.
            print(evento)
            #Catch mouse position and if it's pressed on the button
            if evento.type == pygame.MOUSEBUTTONDOWN:
                #scene handler
                #here we check where the story line of the game is and define some button presses to make it more functional.
                if define_location == "main_menu":
                    if pygame.mouse.get_pos()[0] >= 330 and pygame.mouse.get_pos()[1] >= 380:
                        if pygame.mouse.get_pos()[0] <= 598 and pygame.mouse.get_pos()[1] <= 445:
                            define_location = "select_planet"
                    if pygame.mouse.get_pos()[0] >= 330 and pygame.mouse.get_pos()[1] >= 600:
                        if pygame.mouse.get_pos()[0] <= 600 and pygame.mouse.get_pos()[1] <= 665:
                            main_loop = False
                #buttons and other story line scripts can be placed here
                elif define_location == "select_planet":
                    if pygame.mouse.get_pos()[0] >= 5 and pygame.mouse.get_pos()[1] >= 5:
                        if pygame.mouse.get_pos()[0] <= 155 and pygame.mouse.get_pos()[1] <= 53:
                            define_location = "main_menu"         
                    if pygame.mouse.get_pos()[0] >= 708 and pygame.mouse.get_pos()[1] >= 335:
                        if pygame.mouse.get_pos()[0] <= 855 and pygame.mouse.get_pos()[1] <= 473:
                            define_location = "planet_astrodoge"
                    if pygame.mouse.get_pos()[0] >= 186 and pygame.mouse.get_pos()[1] >= 412:
                        if pygame.mouse.get_pos()[0] <= 263 and pygame.mouse.get_pos()[1] <= 494:
                            define_location = "planet_spacestrike"
                    if pygame.mouse.get_pos()[0] >= 630 and pygame.mouse.get_pos()[1] >= 637:
                        if pygame.mouse.get_pos()[0] <= 720 and pygame.mouse.get_pos()[1] <= 722:
                            define_location = "planet_3"
                            # planet Eva
                            # rechts onderin 
                    if pygame.mouse.get_pos()[0] >= 596 and pygame.mouse.get_pos()[1] >= 5:
                        if pygame.mouse.get_pos()[0] <= 693 and pygame.mouse.get_pos()[1] <= 71:
                            define_location = "planet_4"
                            #planet Kimberly
                            #Boven aan het scherm
                            print('planet_4')
                    if pygame.mouse.get_pos()[0] >= 21 and pygame.mouse.get_pos()[1] >= 557:
                        if pygame.mouse.get_pos()[0] <= 86 and pygame.mouse.get_pos()[1] <= 627:
                            define_location = "planet_5" 
                            #planet Davin
                            # links onder 
                            print('planet_5')       
 
        pygame.display.flip()
    pygame.quit()
    quit()
