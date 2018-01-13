#This script is for playing and moving around a sprite
#import all lib's + intergratie
heart_amount = 3
def start_spacestrike():
    import pygame
    import random
    import os
    import menu
    import highscore
    import game_over
    import soundboard

    #set x and y of the window on screen. (EXPIRIMENTAL)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)


    #Start Pygame
    pygame.init() 
    #init the sound libs of pygame.
    soundboard.spst_main()
    #Defineeer de groote en breedte van de game
    screen = pygame.display.set_mode((900, 900))
    #Verander titel
    pygame.display.set_caption("SPACESTRIKE")
    #Setup voor de fps 
    clock = pygame.time.Clock()
    # images for the background
    surface = pygame.image.load('resource/images/spacestrike/background/background_splaceholder.png').convert()
    surface_rect = surface.get_rect()
    print (surface)
    print (surface_rect)
    #load in font
    font = pygame.font.Font('resource/fonts/Arcadepix.ttf', 30)
    #load in all sprites
    bullet_sound = pygame.mixer.Sound('resource/music/splaceholder/sounds/sfx_wpn_laser10.wav')

    #de main game loops
    running = True
    while running:
        while pause == True:
            clock.tick(FPS)
            mm_button        = pygame.image.load('resource/images/pause_screen/button_mm.png').convert()
            resume_button    = pygame.image.load('resource/images/pause_screen/button_resume.png').convert()
            restart_button   = pygame.image.load('resource/images/pause_screen/button_restart.png').convert()
            mm_rect          = mm_button.get_rect()
            resume_rect      = resume_button.get_rect()
            restart_rect     = restart_button.get_rect()
            screen.blit(mm_button, (325,550))
            screen.blit(resume_button, (325,470))
            screen.blit(restart_button, (325,390))

            for event in pygame.event.get():
                print (event)
                #Check of de exit knop is ingedrukt
                if event.type == pygame.QUIT:
                    running = False

                #als esc ingedrukt wordt pauseert het spel
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = False
                        soundboard.resume()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 325 and pygame.mouse.get_pos()[1] >= 550:
                        if pygame.mouse.get_pos()[0] <= 593 and pygame.mouse.get_pos()[1] <= 615:
                            menu.start_menu()
                    if pygame.mouse.get_pos()[0] >= 325 and pygame.mouse.get_pos()[1] >= 470:
                        if pygame.mouse.get_pos()[0] <= 593 and pygame.mouse.get_pos()[1] <= 535:
                            pause = False
                            soundboard.resume()
                    if pygame.mouse.get_pos()[0] >= 325 and pygame.mouse.get_pos()[1] >= 390:
                        if pygame.mouse.get_pos()[0] <= 593 and pygame.mouse.get_pos()[1] <= 455:
                            print('goes to cheet sheet.')
            #flip the display.
            pygame.display.flip()

        while pause == False:
          
            # Laat de clock ticken op de fps
            clock.tick(FPS)

            #kijk of er een event is 
            for event in pygame.event.get():
                print (event)
                #Check of de exit knop is ingedrukt
                if event.type == pygame.QUIT:
                    running = False
                #Catch mouse position and if it's pressed on the button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 5 and pygame.mouse.get_pos()[1] >= 5:
                        if pygame.mouse.get_pos()[0] <= 155 and pygame.mouse.get_pos()[1] <= 53:
                           menu.start_menu()

                #als spatie word ingedrukt moet er een kogel afgeschoten worden
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet_sound.play()
                        player.shoot()
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                        soundboard.pause()
                        # pygame.mixer.Sound.play()
            #update
            all_sprites.update()

            #collision for bullet against enemy
            hits = pygame.sprite.groupcollide(enemys, bullets, True, True)
            if hits:
                score += 100
                soundboard.bullet_on_hit_enemy()
            for hit in hits:
                m = enemy()
                all_sprites.add(m)
                enemys.add(m)

            #collision if player hits enemys
            hits = pygame.sprite.spritecollide(player, enemys, True, pygame.sprite.collide_circle)
            if hits:
                soundboard.bullet_on_hit_friendly()
                lose_heart()

            #collision if enemy bullet hits player
            hits = pygame.sprite.spritecollide(player, en_bullets, True, pygame.sprite.collide_circle)
            if hits:
                soundboard.bullet_on_hit_friendly()
                lose_heart()
            
            def lose_heart():
                global heart_amount
                heart_amount -= 1

            #draw / render
            if start_init == True:
                screen.fill(BLACK)
                start_init = False
            screen.blit(surface, surface_rect)
            
            quit_button         = pygame.transform.scale(pygame.image.load ('resource/images/select_planet/button_quit_small.png'), (42,40))
            quit_rect           = quit_button.get_rect()
            screen.blit(quit_button, (5,5))    
            
            #check lives, else load game over screen
            if heart_amount == 3:
                hearts = pygame.transform.scale(pygame.image.load ('resource/UI/spacestrike/heart_3.png'), (130,45))
                screen.blit(hearts, [365, 0])
            elif heart_amount == 2:
                hearts = pygame.transform.scale(pygame.image.load ('resource/UI/spacestrike/heart_2.png'), (130,45))
                screen.blit(hearts, [365, 0])
            elif heart_amount == 1:
                hearts = pygame.transform.scale(pygame.image.load ('resource/UI/spacestrike/heart_1.png'), (130,45))
                screen.blit(hearts, [365, 0])
            else:
                print('game over')
                game_over.start(score, 2)
                

            scoretext = font.render("Score :  {0}".format(score), 1, WHITE)
            screen.blit(scoretext, (720, 10))
            

            all_sprites.draw(screen)

            #flip the display.
            pygame.display.flip()

    pygame.quit()

    #start_spacestrike()