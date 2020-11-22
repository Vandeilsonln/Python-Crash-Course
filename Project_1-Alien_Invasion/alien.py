import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''A class to represent a single alien in the fleet.'''

    def __init__(self, ai_settings, screen):
        # Initialize the alienand set its starting position.
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect atribute.
        self.image = pygame.image.load('./Project_1-Alien_Invasion/_images/alien.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        # Draw the alien at its current location.
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        # Move alien left or right
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
    
    def has_alien_reach_edge(self):
        # Return TRue if alien is at edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        