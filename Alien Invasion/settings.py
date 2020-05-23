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
        self.kb_show_stats = pygame.K_s
        self.kb_quit = pygame.K_q

        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (160, 60, 60)
        #self.bullet_image = pygame.image.load('Alien Invasion\\images\\ship_missile.png')
        #self.bullet_rect = self.bullet_image.get_rect()
        self.max_bullets = 5 # with the current system it creates a visual error

        # Ship settings
        self.ship_limit = 3

        # Alien settings
        self.fleet_drop_speed = 20

        # Game speed
        self.speedup_scale = 1.1

        # Alien points
        self.score_scale = 2
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change durring the game"""

        self.ship_speed = 0.75
        self.bullet_speed = 2.5
        self.alien_speed = 0.3

        # Fleet direction. 1 represents right, -1 represents left
        self.alien_direction = 1

        # Scoring
        self.alien_points = 10

    def increase_speed(self):
        """Increase speed settings and alien points value"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
