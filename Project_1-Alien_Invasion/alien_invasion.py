import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize game, settings and screen object.
    pygame.init()
    mySettings = Settings()
    
    # Make a screen
    myScreen = pygame.display.set_mode((mySettings.screen_width, mySettings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make the Play! button
    play_button = Button(mySettings, myScreen,"Play!")

    # Crete an instance to store game statistics and create a scoreboard
    stats = GameStats(mySettings)
    sb = Scoreboard(myScreen, myScreen, stats)

    # Make a ship
    ship = Ship(mySettings, myScreen)

    # Make a group to store bullets in.
    bullets = Group()

    # Make a group to store the alien fleet.
    aliens = Group()

    # Create the fleet of aliens.

    gf.create_fleet(mySettings, myScreen, aliens, ship)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(mySettings, myScreen, ship, bullets, stats, play_button, aliens=aliens, sb=sb)   # Handles keyboard

        if stats.game_active:
            ship.update_ship_position()
            gf.update_bullets(aliens, bullets, myScreen, ship, mySettings, stats, sb)
            gf.update_aliens(mySettings, aliens, ship, stats, bullets, myScreen)
        
        gf.update_screen(mySettings, myScreen, ship, bullets, aliens, play_button, stats, sb)    # Blit ship, background and update screen  

        # make the most recently drawn screen visible.
        pygame.display.flip()


run_game()