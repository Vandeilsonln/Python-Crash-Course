#! python3

# blueSky.py - Create a Pygame window with a blue background

import pygame

def createWindow():
    pygame.init()   # initialize pygame
    myScreen = pygame.display.set_mode((800, 680))  # windows size
    pygame.display.set_caption('Blue Sky') # window title
    
    """
    # Create background with color

    myScreen.fill((0, 0, 230)) # Set up background color
    """

    # Create background with a image
    bg = pygame.image.load('./exercises/images/game_bg.jpg')

    while True:
        pygame.display.flip()   # show the most recent screen


createWindow()