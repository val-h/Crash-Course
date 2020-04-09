class GameStats:
    """Track statistics about the game"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """reset the statistics"""
        self.ships_left = self.settings.ship_limit
