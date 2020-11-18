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

# Set up character class
class Character():
    def __init__(self, screen):
        self.myChar = pygame.image.load('./Project_1-Alien_Invasion/exercises/images/game_char.png')

        # Get size of the character
        self.char_size = self.myChar.get_rect()
        self.screen_size = screen.get_rect()

        # Set initial position
        self.char_size.centerx = self.screen_size.centerx
        self.char_size.centery = self.screen_size.centery


# Place it on the screen
mainChar = Character(myScreen)
myScreen.blit(mainChar.myChar, mainChar.char_size)
# While loop
while True:
    pygame.display.flip()   # show the most recent screen