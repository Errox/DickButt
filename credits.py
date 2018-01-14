def start():
    #defining every library needed
    import sys
    import pygame
    import os
    import menu
    import soundboard
    from time import sleep

    #setting variables
    FPS     = 30
    X       = 500
    Y       = 100
    WHITE   = (255, 255, 255)
    BLACK   = (0, 0, 0)
    pygame.init()
    #setting the settings of pygame itself
    screen = pygame.display.set_mode((900,900))
    pygame.display.set_caption("Jup, those people made it")
    clock = pygame.time.Clock()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
    define_location = "main_menu"
    soundboard.credits_theme()
    text_list = '''This game is made by:
    Ryan Groenewold -> Astrododge, intergration of all games, 
    highscores, sounds, Health bar mechanics, 
    "cheat sheets / explaination screen" mechanic
    _______________________________
    Laura Young -> SpaceStrike, credits, All sprites in game,
    Intergration, Documentation, 
    score in individiual games
    _______________________________
    Eva Wegman -> Spacebound
    _______________________________
    Kimberly Schoenaker -> Invasion of the Unkown.
    _______________________________ 
    Davin Essenius -> Stranded
    _______________________________

    text_list = All sounds, images and mechanics are used for personal use.
    We don't own any of the coprights of any of these objects

    '''.split('\n')


    class Credits:
        def __init__(self, screen_rect, lst):
            self.srect = screen_rect
            self.lst = lst
            self.size = 30
            self.color = (255,255,255)
            self.buff_centery = self.srect.height/2 + 5
            self.buff_lines = 50
            self.timer = 0.0
            self.delay = 50
            self.make_surfaces()


        def make_text(self,message):
            font = pygame.font.Font('resource/fonts/Arcadepix.ttf', self.size)
            text = font.render(message,True,self.color)
            rect = text.get_rect(center = (self.srect.centerx, self.srect.centery + self.buff_centery) )
            return text,rect

        def make_surfaces(self):
            self.text = []
            for i, line in enumerate(self.lst):
                l = self.make_text(line)
                l[1].y += i*self.buff_lines
                self.text.append(l)

        def update(self):
            if pygame.time.get_ticks()-self.timer > self.delay:
                self.timer = pygame.time.get_ticks()
                for text, rect in self.text:
                    rect.y -= 1

        def render(self, surf):
            for text, rect in self.text:
                surf.blit(text, rect)

    quit_button         = pygame.transform.scale(pygame.image.load ('resource/images/select_planet/button_quit_small.png'), (42,40))
    quit_rect           = quit_button.get_rect()
    background = pygame.image.load('resource/images/game_over/game_overbg.png').convert()
    background_rect = background.get_rect()
    #beginning of the main loop
    main_loop = True
    screen_rect = screen.get_rect()
    cred = Credits(screen_rect, text_list)
    while main_loop:
        #reset the screen and set screen image's
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        screen.blit(quit_button, (0,0))
        clock.tick(FPS)
        cred.update()
        cred.render(screen)
        #check events
        for evento in pygame.event.get():
            #define event's of quiting the game.
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 5 and pygame.mouse.get_pos()[1] >= 5:
                    if pygame.mouse.get_pos()[0] <= 155 and pygame.mouse.get_pos()[1] <= 53:
                        menu.start_menu()
            print(evento)
        pygame.display.flip()

    pygame.quit()
    quit()
