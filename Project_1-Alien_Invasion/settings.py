import pygame

class Settings():
    # A class to store all settings for Alien Invasion.

    def __init__(self):
        # Screen Settings.
        self.screen_width = 1080
        self.screen_height = 620
        self.bg_image = pygame.image.load('Project_1-Alien_Invasion/_images/background_stars.jpg')