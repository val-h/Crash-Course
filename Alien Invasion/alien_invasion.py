import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
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

        self.ship = Ship(self)
        self.charecter = Charecter(self)
        
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        print('Starting the game')
        while True:
            self._check_events()
            self.ship.update()
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

    def _update_screen(self):
        """Update images to the screen, and flip to the new screen"""
        # Set the bg_color
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.charecter.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Making na instance of the game and running it
    ai = AlienInvasion()
    ai.run_game()
