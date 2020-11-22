import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # A class to manage bullets fired from the ship.

    def __init__ (self, ai_settings, screen, ship):
        # Create a bullet object at the ship's current position.
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0,0) and then set current position.
        self.bullet_rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) # TODO: Replace this RECT object for an bullet image.
        self.rect = self.bullet_rect
        self.bullet_rect.centerx = ship.rect.centerx
        self.bullet_rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.bullet_rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # Move the bullet up the screen

        # Update the decimal position of the bullet.
        self.y -= self.speed_factor

        # Update the rect position.
        self.bullet_rect.y = self.y
        
    def draw_bullet(self):
        # Draw the bullet to the screen.
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)    # TODO: use self.screen.blit() method to place an image instead of a rect.
            