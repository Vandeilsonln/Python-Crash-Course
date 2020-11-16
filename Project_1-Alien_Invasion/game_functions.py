#! python3

import sys, pygame

def check_events(ship):
    # Respond to kaypresses and mouse events.
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    # Update images on the screen and flip to the new screen.
    # Redraw the screen during each pass through the loop.
        #screen.fill(ai_settings.bg_color)
        screen.blit(pygame.image.load('_images/background_stars.jpg').convert(), [0, 0])
        ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
