class Settings:
    """A class to store all the settings for the game."""
    def __init__(self):
        """Initialize the game settings."""

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (77, 166, 255)

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
