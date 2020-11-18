import sys, pygame


def check_keydown_events(event, ship):
    # Respond to keypresses.
    if event.key == pygame.K_RIGHT:
        # Move ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move ship to teh left
        ship.moving_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # Stop moving to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Stop moving to the left
        ship.moving_left = False

def check_events(ship):
    # Respond to keypresses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(settings, screen, ship):
    # Update images on the screen and flip to the new screen.
    screen.blit(settings.bg_image.convert(), [0, 0])  # Blit background
    ship.blitme()   # Blit ship

    # Make the most recently drawn screen visible.
    pygame.display.flip()