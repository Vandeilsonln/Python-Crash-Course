import sys, pygame


def check_events():
    # Respond to keypresses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, ship):
    # Update images on the screen and flip to the new screen.
    screen.blit(settings.bg_image.convert(), [0, 0])  # Blit background
    ship.blitme()   # Blit ship

    # Make the most recently drawn screen visible.
    pygame.display.flip()