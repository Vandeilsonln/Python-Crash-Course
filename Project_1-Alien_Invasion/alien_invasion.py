import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien


def run_game():
    # Initialize game, settings and screen object.
    pygame.init()
    mySettings = Settings()
    
    # Make a screen
    myScreen = pygame.display.set_mode((mySettings.screen_width, mySettings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make a ship
    ship = Ship(mySettings, myScreen)

    # Make a group to store bullets in.
    bullets = Group()

    # Make an alien.
    alien = Alien(mySettings, myScreen)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(mySettings, myScreen, ship, bullets)   # Handles keyboard
        ship.update_ship_position()
        gf.update_bullets(bullets) 
        gf.update_screen(mySettings, myScreen, ship, bullets, alien)    # Blit ship, background and update screen  

        # make the most recently drawn screen visible.
        pygame.display.flip()


run_game()