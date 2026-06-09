from random import random


def spin_row():
    symbols = [" 🍒", " 🍋", " 🍉", " 🔔", " ⭐"]
    return [symbols(int(random() * len(symbols))) for _ in range(3)]

def print_row(row):
    print("******************")
    print(" | ".join(row))
    print("******************")
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == " 🔔":
            return bet * 10
        elif row[0] == " ⭐":
            return bet * 20
    return 0

def main():
    balance = 100
    print("****************************")
    print("Welcome to the Python Slot!")
    print("Symbols: 🍒, 🍋, 🍉,🔔,⭐")
    print(f"Your balance is ${balance}")
    print("****************************")
    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = int(input("Enter your bet amount: "))
        if not bet.is_integer():
            print("Please enter a valid number.")
            continue
        bet = int(bet)
        if bet > balance:
            print("You don't have enough balance to place that bet.")
            continue
        if bet <= 0:
            print("Bet must be greater than zero.")
            continue
        balance -= bet
        row = spin_row()
        print("Spinning...")
        print_row(row)
        
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You win ${payout}")
        else:
            print("Sorry, you lost this bet")
        balance += payout
        play_again = input("Do you want to play again(Y/N).")
        if play_again.lower() != "y":
            print(f"Thanks for playing! Your final balance is ${balance}")
            break
        else:
            print("Good luck on the next spin!")

if __name__ == "__main__":
    main()