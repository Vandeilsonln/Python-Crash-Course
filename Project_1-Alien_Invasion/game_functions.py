import sys, pygame
from bullet import Bullet
from alien import Alien
from time import sleep


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

def check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens):
    # Respond to keypresses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, ai_settings, screen, ship, aliens, bullets)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen, ship, bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_play_button(stats, play_button, mouse_x, mouse_y, ai_settings, screen, ship, aliens, bullets):
    # Start a new game when the player clicks Play
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens)
        ship.center_ship()

def update_screen(settings, screen, ship, bullets, alien, play_button, stats, sb):
    # Update images on the screen and flip to the new screen.
    screen.blit(settings.bg_image.convert(), [0, settings.bg_initial_position])  # Blit background

    # Move background
    move_background(settings)    

    # Redraw all bullets hebind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()   # Blit ship
    alien.draw(screen)  # Draw fleet of alien on the screen

    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def move_background(settings):
    if settings.bg_initial_position < 0:
        settings.bg_initial_position += settings.bg_moving_speed
    else:
        settings.bg_initial_position = -1705

def update_bullets(aliens, bullets, screen, ship, ai_settings, stats, sb):
    # Update position of bullets and get rid of old bullets.
    
    # Update bullet position.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.bullet_rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_colisions(ai_settings, screen, ship, aliens, bullets, stats, sb)

def check_bullet_alien_colisions(ai_settings, screen, ship, aliens, bullets, stats, sb):
    # Respond to bullet-alien colisions.
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

    if len(aliens) == 0:
        # Destroy existing bullets, speed up the game and create new fleet.
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, aliens, ship)

def get_number_aliens_x(ai_settings, alien_width, factor):
    # Determine the numer of aliens that fit in a row.
    available_space_x = ai_settings.screen_width - factor * alien_width
    number_aliens_x = int(available_space_x / (factor * alien_width))

    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    # Determine the number of rows of aliens that fit on the screen.
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)

    number_rows = int(available_space_y / (2.5 * alien_height))

    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, factor, row_number):
    # Create an alien and place it in the row.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + factor * alien_width * alien_number

    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + factor * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
    """Create a full fleet of aliens."""

    # Create an alien and find the number of aliens in a row.
    alien_factor = 1.6
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width, alien_factor)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row
            create_alien(ai_settings, screen, aliens, alien_number, alien_factor, row_number)
    
def update_aliens(ai_settings, aliens, ship, stats, bullets, screen):
    # Check if the fleet is at and edge, and then update the position of all aliens in the fleet
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_was_hit(ai_settings, stats, screen, ship, aliens, bullets)
    
    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    # Respond appropriately if any aliens have reached an edge
    for alien in aliens.sprites():
        if alien.has_alien_reach_edge():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    # Drop the entire fleet and change the fleet's direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_was_hit(ai_settings, stats, screen, ship, aliens, bullets):
    # Respond to ship being hit by alien
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        # Pause.
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    # Check if any aliens have reached the bottom of the screen
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # treat this the same as if the ship got hit
            ship_was_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
