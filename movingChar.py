#! python3

# movingChar.py - Create a game with a background and an character. Make it move through the screen and set edge limits.


import pygame


# Set up game
pygame.init()

# Set up background
myScreen = pygame.display.set_mode((1024, 626)) # screen size
pygame.display.set_caption('Moving Character')  # screen title
gameBg = pygame.image.load('./Project_1-Alien_Invasion/exercises/images/game_bg.jpg')   # load background image
myScreen.blit(gameBg, [0, 0])   # draw background image

# Set up character

# Place it on the screen

# While loop
while True:
    pygame.display.flip()   # show the most recent screen