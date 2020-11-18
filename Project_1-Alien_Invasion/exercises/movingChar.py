import pygame, sys


# Set up pygame
pygame.init()

# Create a screen
myScreen = pygame.display.set_mode((1004, 626))
pygame.display.set_caption('Moving character')

# Create a background
bg_image = pygame.image.load('./Project_1-Alien_Invasion/exercises/images/game_bg.jpg')

# Create a character class
class Character():
    def __init__(self, screen)
    
    self.char_image = pygame.image.load('./Project_1-Alien_Invasion/exercises/images/game_char.png')
    self.screen = screen

    # Get the character rect
    self.char_rect = self.char_image.get_rect()
    # Get the screen rect
    self.screen_rect = self.screen.get_rect()

    # Initialize the char image on the center of the screen
    self.char_rect.centerx = self.screen_rect.centerx
    self.char_rect.centery = self.screen_rect.centery

    # Create flags to allow continuous movement
    self.moving_right = False
    self.moving_left = False
    self.moving_up = False
    self.moving_down = False

    # Character speed
    self.char_speed = 2


    def update_char_position(event, char):
        # It will set the flags to true based on which event was passed.
        if self.moving_left and self.char_rect.left > 0:
            self.char_rect.centerx -= self.char_speed
        
        if self.moving_right and self.char_rect.right < self.screen_rect.right:
            self.char_rect.centerx += self.char_speed
        
        if self.moving_up and self.char_rect.up > 0:
            self.char_rect.centery -= self.char_speed
        
        if self.moving_down and self.char_rect.bottom < self.screen_rect.bottom:
            self.char_rect.centery += self.char_speed


# Create Character
myChar = Character(myScreen)

# Function to handle events
def check_keydown_event(event, char):
    if event.key == pygame.K_LEFT:
        char.moving_left = True
    elif event.key == pygame.K_RIGHT:
        char.moving_right = True
    elif event.key == pygame.K_UP:
        char.moving_up = True
    elif event.key == pygame.K_DOWN:
        char.moving_down = True

def check_keyup_event(event, char):
    if event.key == pygame.K_LEFT:
        char.moving_left = False
    elif event.key == pygame.K_RIGHT:
        char.moving_right = False
    elif event.key == pygame.K_UP:
        char.moving_up = False
    elif event.key == pygame.K_DOWN:
        char.moving_down = False

def check_events(char):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, char)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, char)

while True:
    # Check for keyboard presses

    # Update the position


    # Blit background and ship

    # Show the most recently drawn screen
    pygame.display.flip()