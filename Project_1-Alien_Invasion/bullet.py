import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # A class to manage bullets fired from the ship.

    def __init__ (self, ai_settings, screen, ship):
        # Create a bullet object at the ship's current position.
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0,0) and then set current position.
        self.bullet_rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.bullet_rect.centerx = ship.rect.centerx
        self.bullet_rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.bullet_rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        