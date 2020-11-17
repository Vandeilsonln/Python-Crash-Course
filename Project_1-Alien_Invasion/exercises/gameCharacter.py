#! python3
# gameCharacter.py - Create a window and a character. Draw the character into the screen

import pygame


class Character():
    def __init__(self, screen):
        self.screen = screen

        # Set up the character image
        self.character = pygame.image.load('./Project_1-Alien_Invasion/exercises/images/game_char.png')

        # Get both character and screen sizes (rect)
        self.char_size = self.character.get_rect()
        self.screen_size = self.screen.get_rect()

        # Set position of the char on the screen
        self.char_size.left = self.screen_size.left + 50
        self.char_size.centery = self.screen_size.centery


# Create a window
pygame.init()
myScreen = pygame.display.set_mode((1004, 626))
pygame.display.set_caption('Game with a Character')

# Set up the background with an image.
game_background = pygame.image.load('./Project_1-Alien_Invasion/exercises/images/game_bg.jpg')
myScreen.blit(game_background, [0, 0])

# Draw the character
myChar = Character(myScreen)
myScreen.blit(myChar.character, myChar.char_size)

# Infinite loop
while True:
    pygame.display.flip()   # Shows the most recent screen

    