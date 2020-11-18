import sys, pygame
from settings import Settings

def run_game():
    # Initialize game, settings and screen object.
    pygame.init()
    mySettings = Settings()
    myScreen = pygame.display.set_mode((mySettings.screen_width, mySettings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Redraw the screen during each pass through the loop.
        myScreen.blit(mySettings.bg_image, [0, 0])
        # make the most recently drawn screen visible.
        pygame.display.flip()


run_game()