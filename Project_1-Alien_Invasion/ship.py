import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings , screen):
        # Initialize the ship and set it's starting position.
        super().__init__()
        self.screen = screen
        self.settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('./Project_1-Alien_Invasion/_images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center_position = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update_ship_position(self):
        # Update the SHIP'S POSITION CENTER VALUE. NOT THE RECT!
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_position += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_position -= self.settings.ship_speed_factor
        
        # Update RECT OBJECT from self.center_position.
        self.rect.centerx = self.center_position
    
    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        # Center the ship on the screen.
        self.center = self.screen_rect.centerx