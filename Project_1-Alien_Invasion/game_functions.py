import sys, pygame
from bullet import Bullet
from alien import Alien


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

def update_screen(settings, screen, ship, bullets, alien):
    # Update images on the screen and flip to the new screen.
    screen.blit(settings.bg_image.convert(), [0, settings.bg_initial_position])  # Blit background

    # Move background
    move_background(settings)    

    # Redraw all bullets hebind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()   # Blit ship
    alien.draw(screen)  # Draw fleet of alien on the screen

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def move_background(settings):
    if settings.bg_initial_position < 0:
        settings.bg_initial_position += settings.bg_moving_speed
    else:
        settings.bg_initial_position = -1705

def update_bullets(bullets):
    # Update position of bullets and get rid of old bullets.

    # Update bullet position.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.bullet_rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(ai_settings, alien_width, factor):
    # Determine the numer of aliens that fit in a row.
    available_space_x = ai_settings.screen_width - factor * 
    number_aliens_x = int(available_space_x / (factor * alien_width))

    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, factor):
    # Create an alien and place it in the row.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + factor * alien_width * alien_number

    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens."""

    # Create an alien and find the number of aliens in a row.
    alien_factor = 1.6
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width, alien_factor)

    # Create the first row of aliens.
    for alien_number in range(number_aliens_x):
        # Create an alien and place it in the row
       create_alien(ai_settings, screen, aliens, alien_number, alien_factor)
