import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

from charecter import Charecter


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create the game resources."""
        pygame.init()
        self.settings = Settings()

        # Setting the display
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.stats = GameStats(self)
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
        # self.charecter = Charecter(self)

    def run_game(self):
        """Start the main loop for the game."""
        print('Starting the game')
        while True:
            self._check_events()
            self.ship.update()
            self._update_aliens()
            self._update_bullets()
            self._update_screen()
            
    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Quiting Alien Invasion...')
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
        
    def _check_keydown_events(self, event):
        """Respond to keydown events"""

        # Ship movement
        if event.key == self.settings.kb_right:
            self.ship.move_right = True
        elif event.key == self.settings.kb_left:
            self.ship.move_left = True
        
        # Firing bullets
        if event.key == self.settings.kb_fire:
            self._fire_bullet()

        # Game Interface
        if event.key == self.settings.kb_quit:
            print('Quiting Alien Invasion...')
            sys.exit()
    
    def _check_keyup_events(self, event):
        """Respond to keyup events"""
        if event.key == self.settings.kb_right:
            self.ship.move_right = False
        elif event.key == self.settings.kb_left:
            self.ship.move_left = False
        
    def _ship_hit(self):
        """Respond to the ship being hit by aliens"""
        
        # Decrement the ships left
        self.settings.ship_limit -= 1

        # Remove all of the bullets and aliens
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet an center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Pause
        sleep(0.5)
    
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites:
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat the case the same way as if the ship got hit
                self._ship_hit()
                break
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.max_bullets:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Updates to the bullets in the game"""
        # Update the bullets possition
        self.bullets.update()

        # Getting rid of bullets that had disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Check the collisions between the bullets and aliens"""
        # Add the aliens and bullets to a group and check if they collide,
        # if so remove the bullet and alien. Posible feature is an explosion
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)

        # Check if the fleet is destroyed, remove all bullets and spawn a new fleet
        if not self.aliens:
            self.bullets.empty
            print('Round won!')
            self._create_fleet()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien instance and find the number of aliens in a row
        # Spacing between each alien is equal to a half of the alien's width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - alien_width
        number_aliens_x = available_space_x // (2 * alien_width)

        # Vertical spacing
        available_space_y = self.settings.screen_height - (3 * alien_height) - self.ship.rect.height
        row_number = available_space_y // (2 * alien_height)

        # Create the first row of aliens
        for alien_row in range(row_number):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, alien_row)

    def _create_alien(self, alien_number, row_number):
        """Create a single alien and place it in the fleet"""
        # Create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = 2 * alien_width * alien_number + 20
        alien.rect.x = alien.x
        alien.y = 2 * alien_height * row_number + 20
        alien.rect.y = alien.y
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """Responding to every alien that reaches the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._check_fleet_direction()
                break
    
    def _check_fleet_direction(self):
        """Drop the fleet and change its direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.alien_direction *= -1

    def _update_aliens(self):
        """
        Check if the fleet hits an edge,
        update the possition of all the aliens in the group"""
        self._check_fleet_edges()
        self.aliens.update()

        # Check if the ship collided with an alien
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print('Ship hit!')
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _update_screen(self):
        """Update images to the screen, and flip to the new screen"""
        # Set the bg_color
        self.screen.blit(self.settings.bg_image, (0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()
        #self.charecter.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Making na instance of the game and running it
    ai = AlienInvasion()
    ai.run_game()
