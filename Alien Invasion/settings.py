import pygame

class Settings:
    """A class to store all the settings for the game."""
    def __init__(self):
        """Initialize the game settings."""

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_image = pygame.image.load('Alien Invasion\\images\\ai_bg.png')
        self.bg_color = (77, 166, 255)

        # Key bindings
        self.kb_right = pygame.K_d
        self.kb_left = pygame.K_a
        self.kb_fire = pygame.K_SPACE
        self.kb_quit = pygame.K_q

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (160, 60, 60)
        #self.bullet_image = pygame.image.load('Alien Invasion\\images\\ship_missile.png')
        #self.bullet_rect = self.bullet_image.get_rect()
        self.max_bullets = 5 # with the current system it creates a visual error

        # Ship settings
        self.ship_speed = 0.75
        self.ship_limit = 3

        # Alien settings
        self.alien_speed = 1.5
        self.fleet_drop_speed = 20
        self.alien_direction = 1
