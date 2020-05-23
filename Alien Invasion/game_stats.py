import json

hs_filename = 'Alien Invasion\highscore.json'

class GameStats:
    """Track statistics about the game"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the game in an active state
        self.game_active = False

        # High score
        with open(hs_filename) as f:
            self.high_score = json.load(f)
    
    def reset_stats(self):
        """reset the statistics"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

        self.fleet_count = 0

        self.shots_fired = 0
        #self.aliens_hit = 0
    
    def update_highscore(self):
        """Updates the highscore value to a json file"""
        with open(hs_filename, 'w') as f:
            json.dump(self.high_score, f)
