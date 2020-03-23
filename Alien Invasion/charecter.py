import pygame

class Charecter:
    """Creating a simple charecter with a sprite and a possition."""

    def __init__(self, ai_game):
        """Initialization of the charecter."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loading the image and its form/rect
        self.image = pygame.image.load('Alien Invasion\\images\\charecte.png')
        self.charecter_rect = self.image.get_rect()

        # Set the possition of the charecter
        self.charecter_rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the charecter at a specific possition."""
        self.screen.blit(self.image, self.charecter_rect)
