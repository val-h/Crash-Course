import pygame

class Ship:
    """Creating a ship with functions to manage it."""

    SHIP_SPEED = 0.3

    def __init__(self, ai_game):
        """Creating the ship and manage its possition."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('Alien Invasion\\images\\ship.png')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Current x position of the ship
        self.x = float(self.rect.x)

        # Movement flags
        self.move_right = False
        self.move_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's possition based on the movement flag."""
        if self.move_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.SHIP_SPEED
        if self.move_left == True and self.rect.left > 0:
            self.x -= self.SHIP_SPEED

        self.rect.x = self.x
