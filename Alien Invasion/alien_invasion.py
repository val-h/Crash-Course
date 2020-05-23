import sys
from time import sleep
import json

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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
        self.sb = Scoreboard(self)
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make the play button
        self.play_button = Button(self, 'Play')
        
        # self.charecter = Charecter(self)

    def run_game(self):
        """Start the main loop for the game."""
        print('Starting the game')
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()
            
            self._update_screen()
            
    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Quiting Alien Invasion...')
                self.stats.update_highscore()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
        
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
            self.stats.update_highscore()
            sys.exit()
        
        if event.key == self.settings.kb_show_stats:
            self._print_stats()
    
    def _check_keyup_events(self, event):
        """Respond to keyup events"""
        if event.key == self.settings.kb_right:
            self.ship.move_right = False
        elif event.key == self.settings.kb_left:
            self.ship.move_left = False
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game statistics
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Reset the game settings
            self.settings.initialize_dynamic_settings()
        
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _ship_hit(self):
        """Respond to the ship being hit by aliens"""
        
        if self.stats.ships_left > 0:
            # Decrement the ships left and update the scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Remove all of the bullets and aliens
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet an center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)

            # Print the lives left
            print(f'{self.stats.ships_left} lives left.')
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            print('Game Over!')
    
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.max_bullets:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

            # Add the bullet count to the stats
            self.stats.shots_fired += 1

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
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()
            self.sb.check_high_score()

        # Check if the fleet is destroyed, remove all bullets and spawn a new fleet
        if not self.aliens:
            self.bullets.empty
            print('Round won!')
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

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
        
        # Add to the fleet_count stats
        self.stats.fleet_count += 1

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
    
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat the case the same way as if the ship got hit
                self._ship_hit()
                break
            
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
    
    def _print_stats(self):
        """Print the game stats of the game"""
        print(' --- Game Stats --- \n')
        
        print(f'Level - {self.stats.fleet_count}')
        print(f'Lives left - {self.stats.ships_left}')
        print(f'Total shots fired - {self.stats.shots_fired}')
        #print(f'Total aliens hit - {self.stats.aliens_hit}')

    def _update_screen(self):
        """Update images to the screen, and flip to the new screen"""
        # Set the bg_color
        self.screen.blit(self.settings.bg_image, (0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()

        self.sb.show_score()
        
        # Draw the button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        #self.charecter.blitme()

        # Make the most recently drawn screen visible.q
        pygame.display.flip()

if __name__ == '__main__':
    # Making na instance of the game and running it
    ai = AlienInvasion()
    ai.run_game()
