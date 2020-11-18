import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game, settings and screen object.
    pygame.init()
    mySettings = Settings()
    
    myScreen = pygame.display.set_mode((mySettings.screen_width, mySettings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make a ship
    ship = Ship(myScreen)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events()   # Handles keyboard
        
        gf.update_screen(mySettings, myScreen, ship)    # Blit ship, background and update screen  

        # make the most recently drawn screen visible.
        pygame.display.flip()


run_game()