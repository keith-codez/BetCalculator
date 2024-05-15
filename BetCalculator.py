class Bet:
    def __init__(self, stake, odds, type, id):
        self.stake = stake
        self.odds = odds
        self.type = type
        self.id = id

    def display_bet(self):
        return f"Bet:\n Stake: {self.stake}\n Odds: {self.odds}\n BetType: {self.type}\n ID: {self.id}"
    

class Calculator:
    def __init__(self):
        self.bets = []

    def add_bet(self, bet):
        self.bets.append(bet)

    def del_bet(self,id):
        for slip in self.bets:
            if slip.id == id:
                self.bets.remove(slip)
                return f"{id} has been deleted"
        return f"{id} not found..."

    def display(self):
        if not self.bets:
            return f"no bets currently exist"
        return f"\n".join([bet.display_bet() for bet in self.bet])

    def search_bet(self, query):
        found = [slip for slip in self.bets if query.lower() in slip.id ]
        if not found:
            return f"no bets found"
        return f"\n".join([bet.display_bet() for bet in found])

    def save_slips(self, filename="bets.json"):
        data = [{'Stake': bet.stake, 'Odds': bet.odds, 'BetType': bet.type, 'ID': bet.id} for bet in self.bets]
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_bets(self, filename="bets.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.bets = [bet(slip['Stake'], slip['Odds'], slip['BetType'], slip['ID']) for slip in data]
        except FileNotFoundError:
            print("we cannot find this file")


def main():
    calculate = Calculator()

    while True:
        print("\n==== Personal Banking System ===")
        print("1. Add a bet")
        print("2. Remove a bet")
        print("3. Display all bets")
        print("4. Search for a bet")
        print("5. Save all bets")
        print("6. Load saved bets")
        print("7. Exit")
        choice = input("Enter your choice (1....7):")

        if choice=="1":
            stake = input ("Enter the stake: ")
            Odds = input ("Enter the odds: ")
            type = input ("Enter the bet type: ")
            stake = input ("Enter the stake: ")
            stake = input ("Enter the stake: ")
            stake = input ("Enter the stake: ")
            stake = input ("Enter the stake: ")















