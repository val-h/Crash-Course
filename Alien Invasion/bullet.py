import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the bullets frired from the ship."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Creates a bullet at possition (0, 0) and set the correct possition
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
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
        """Draw tje bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
