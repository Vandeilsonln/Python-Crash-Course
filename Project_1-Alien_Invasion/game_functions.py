import sys, pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # Respond to keypresses.
    if event.key == pygame.K_RIGHT:
        # Move ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move ship to teh left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    # Fire a bullet if limit not reached yet.
    # Create a new bullet and add it to the bullets group.
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # Stop moving to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Stop moving to the left
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    # Respond to keypresses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen, ship, bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(settings, screen, ship, bullets):
    # Update images on the screen and flip to the new screen.
    screen.blit(settings.bg_image.convert(), [0, settings.bg_initial_position])  # Blit background

    # Move background
    move_background(settings)    

    # Redraw all bullets hebind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()   # Blit ship

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def move_background(settings):
    if settings.bg_initial_position < 0:
        settings.bg_initial_position += settings.bg_moving_speed
    else:
        settings.bg_initial_position = -360

def update_bullets(bullets):
    # Update position of bullets and get rid of old bullets.

    # Update bullet position.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.bullet_rect.bottom <= 0:
            bullets.remove(bullet)