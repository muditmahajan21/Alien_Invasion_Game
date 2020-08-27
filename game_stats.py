class GameStats:
    #track statistics for the game.

    def __init__(self, ai_game):
        #Initialise statistics.
        self.settings = ai_game.settings
        self.reset_stats()

        #Start game in active state.
        self.game_active = False

        #Hisgh score never to be reset.
        self.high_score = 0

    def reset_stats(self):
        #Initialise stats that can change during the game.
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
