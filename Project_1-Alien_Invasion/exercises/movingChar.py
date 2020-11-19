import pygame, sys
from pygame.sprite import Group

# Set up pygame
pygame.init()

# Create a screen
myScreen = pygame.display.set_mode((1004, 626))
pygame.display.set_caption('Moving character')

# Create a background
bg_image = pygame.image.load('./Project_1-Alien_Invasion/exercises/images/game_bg.jpg')

# Create a character class
class Character():
    def __init__(self, screen):
    
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

    def update_char_position(self):
        # It will set the flags to true based on which event was passed.
        if self.moving_left and self.char_rect.left > 0:
            self.char_rect.centerx -= self.char_speed
        
        if self.moving_right and self.char_rect.right < self.screen_rect.right:
            self.char_rect.centerx += self.char_speed
        
        if self.moving_up and self.char_rect.top > 0:
            self.char_rect.centery -= self.char_speed
        
        if self.moving_down and self.char_rect.bottom < self.screen_rect.bottom:
            self.char_rect.centery += self.char_speed

class Bullets(pygame.sprite.Sprite):
    def __init__(self, character, screen):
        super().__init__()

        self.color = 50, 120, 70
        self.bullet_speed = 1
        self.screen = screen

        # Create a bullet rect and then put it to the right position
        self.bullet_rect = pygame.Rect(0, 0, 20, 12)
        self.bullet_y_position = character.char_rect.centery
        self.bullet_x_position = character.char_rect.right

    def update(self):
        # Move bullet to the right corner
        self.bullet_rect.x += self.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)


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
        print_event(event)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, char)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, char)


# Function to draw screen
def update_screen(char, screen):
    # Blit Background
    screen.blit(bg_image.convert(), [0, 0])

    # Blit character
    screen.blit(myChar.char_image, myChar.char_rect)

# Create Character
myChar = Character(myScreen)

# Create Bullets
myBullets = Group()

while True:
    # Check for keyboard presses
    check_events(myChar)

    # Update character position
    myChar.update_char_position()

    # Update bullet position

    # Blit background, character and bullets
    update_screen(myChar, myScreen)

    # Show the most recently drawn screen
    pygame.display.flip()