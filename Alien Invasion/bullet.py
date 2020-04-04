import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the bullets frired from the ship."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = self.settings.bullet_image

        # Creates a bullet at possition (0, 0) and set the correct possition
        self.rect = self.settings.bullet_rect
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullets possition as a float value
        self.y = float(self.rect.y) 

    def update(self):
        """Move the bullet on the screen."""
        # Update the possition of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect possition
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        self.screen.blit(self.image, self.rect)
