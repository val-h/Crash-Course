import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class responsible for the creation of aliens on the screen."""

    def __init__(self, ai_game):
        """Basic parameters for every alien."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Alien image and rect
        self.image = pygame.image.load('Alien Invasion\\images\\alien.png')
        self.rect = self.image.get_rect()

        # Possition the Alien Ship
        self.rect.x = self.rect.width / 2
        self.rect.y = self.rect.height / 4

        # Current possition of the ship
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the alien"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the possition of the alien on the screen"""
        self.x += self.settings.alien_speed * self.settings.alien_direction
        self.rect.x = self.x
    
    def check_edges(self):
        """Check if the alien hit the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
