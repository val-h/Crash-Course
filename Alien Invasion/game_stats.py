class GameStats:
    """Track statistics about the game"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the game in an active state
        self.game_active = False
    
    def reset_stats(self):
        """reset the statistics"""
        self.ships_left = self.settings.ship_limit

        self.fleet_count = 0

        self.shots_fired = 0
        #self.aliens_hit = 0
