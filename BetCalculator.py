class Bet:
    def __init__(self, stake, odds, type):
        self.stake = stake
        self.odds = odds
        self.type = type

    def display_bet(self):
        