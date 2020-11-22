import pygame

class Settings():
    # A class to store all settings for Alien Invasion.

    def __init__(self):
        # Screen Settings.
        self.screen_width = 1080
        self.screen_height = 630
        self.bg_image = pygame.image.load('Project_1-Alien_Invasion/_images/background_stars_moving.jpg')
        self.bg_moving_speed = 0.2
        self.bg_initial_position = -1705
        
        # Ship Settings
        self.ship_speed_factor = 2.5

        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 130, 60, 60
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 12
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1