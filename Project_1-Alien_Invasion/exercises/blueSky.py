#! python3

# blueSky.py - Create a Pygame window with a blue background

import pygame


def createWindow():
    pygame.init()   # initialize pygame
    myScreen = pygame.display.set_mode((1000, 625))  # windows size
    pygame.display.set_caption('Blue Sky') # window title
    
    """
    # Create background with color

    myScreen.fill((0, 0, 230)) # Set up background color
    """

    # Create background with a image
    bg = pygame.image.load('./Project_1-Alien_Invasion/exercises/images/game_bg.jpg')
    myScreen.blit(bg.convert(), [0, 0])

    while True:
        pygame.display.flip()   # show the most recent screen


createWindow()