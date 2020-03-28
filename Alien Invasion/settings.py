import pygame

class Settings:
    """A class to store all the settings for the game."""
    def __init__(self):
        """Initialize the game settings."""

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (77, 166, 255)

        # Key bindings
        self.kb_right = pygame.K_d
        self.kb_left = pygame.K_a
        self.kb_fire = pygame.K_SPACE
        self.kb_quit = pygame.K_q

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.max_bullets = 3
