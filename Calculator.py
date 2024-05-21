class Bet:
    def __init__(self, stake,type):
        self.stake = stake 
        self.type = type

    def single(self, price):
        returns = (self.stake*price) + self.stake
        return f"your returns are: {returns}" 

    def double(self, price1, price2):
        stage1 = (self.stake*price1) + self.stake
        stage2 = (stage1*price2) + stage1
        return f"Your returns are {stage2}"
    
    def treble(self, price1, price2, price3):
         stage1 = (self.stake*price1) + self.stake
         stage2 = (stage1*price2) + stage1
         stage3 = (stage2*price3) + stage2
         return f"Your returns are {stage3}"
        
def main():
    calculate = Bet()
    while True:
        print("\n==== Bet Calculator Program ===")
        print("1. single bet")
        print("2. double bet")
        print("3. treble bet")
        print("4. Exit")
        choice = input("Enter your choice (1....7):")

        if choice=="1":
            stake = input ("Enter the stake: ")
            Odds = input ("Enter the odds: ")
            type = input ("Enter the bet type: ")
            price = input ("Enter the bet type: ")
            print(calculate.single(price))



    