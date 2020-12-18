import pygame

class Settings():
    # A class to store all settings for Alien Invasion.

    def __init__(self):
        # Screen Settings.
        self.screen_width = 1080
        self.screen_height = 630
        self.bg_image = pygame.image.load('Project_1-Alien_Invasion/_images/background_stars_moving.jpg')
        self.bg_moving_speed = 0.4
        self.bg_initial_position = -1705
        
        # Ship Settings
        self.ship_speed_factor = 1.2
        self.ship_limit = 2

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3 # 3
        self.bullet_height = 15
        self.bullet_color = 130, 60, 60
        self.bullets_allowed = 5 #5

        # Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 30 #15
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.bg_moving_speed = 0.2

        # Fleet_direction of 1 represents right | -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        # Increase speed settings
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bg_moving_speed *= self.speedup_scale