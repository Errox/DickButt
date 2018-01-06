def start_Colour_Select():
#   imports
    import pygame
    import menu
    import pygame.locals
    pygame.init()
#   things
    FPS = 30
    display_width = 900 
    display_height = 900
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Select your colour!')
#   images
    Blue_Char = pygame.image.load('resource/images/Character/Blue/Right/Stance/1.png')
    Green_Char = pygame.image.load('resource/images/Character/Green/Right/Stance/1.png')
    Orange_Char = pygame.image.load('resource/images/Character/Orange/Right/Stance/1.png')
    Pink_Char = pygame.image.load('resource/images/Character/Pink/Right/Stance/1.png')
    Purple_Char = pygame.image.load('resource/images/Character/Purple/Right/Stance/1.png')
    Red_Char = pygame.image.load('resource/images/Character/Red/Right/Stance/1.png')
    Yellow_Char = pygame.image.load('resource/images/Character/Yellow/Right/Stance/1.png')

