from fractions import Fraction
class Bet:
    def __init__(self, stake):
        self.stake = stake

    def single(self, price):
        returns = (self.stake * price) + self.stake
        return f"Your returns are: {returns}"

    def double(self, price1, price2):
        stage1 = (self.stake * price1) + self.stake
        stage2 = (stage1 * price2) + stage1
        return f"Your returns are: {stage2}"

    def treble(self, price1, price2, price3):
        stage1 = (self.stake * price1) + self.stake
        stage2 = (stage1 * price2) + stage1
        stage3 = (stage2 * price3) + stage2
        return f"Your returns are: {stage3}"

def main():
    while True:
        print("\n==== Bet Calculator Program ===")
        print("1. Single bet")
        print("2. Double bet")
        print("3. Treble bet")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            stake = float(input("Enter the stake: "))
            price = input("Enter the selection price (can be a fraction): ")
            price = float(Fraction(price))
            bet = Bet(stake)
            print(bet.single(price))
        elif choice == "2":
            stake = float(input("Enter the stake: "))
            price1 = input("Enter the first selection price (can be a fraction): ")
            price2 = input("Enter the second selection price (can be a fraction): ")
            price1 = float(Fraction(price1))
            price2 = float(Fraction(price2))
            bet = Bet(stake)
            print(bet.double(price1, price2))
        elif choice == "3":
            stake = float(input("Enter the stake: "))
            price1 = input("Enter the first selection price (can be a fraction): ")
            price2 = input("Enter the second selection price (can be a fraction): ")
            price3 = input("Enter the third selection price (can be a fraction): ")
            price1 = float(Fraction(price1))
            price2 = float(Fraction(price2))
            price3 = float(Fraction(price3))
            bet = Bet(stake)
            print(bet.treble(price1, price2, price3))
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


    