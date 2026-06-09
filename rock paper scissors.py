import random

options = ("rock", "paper", "scissors")
player = input("Enter your choice (rock, paper, scissors): ")
computer = random.choice(options)

print(f"Computer chose: {computer}")
print(f"You chose: {player}")

if (computer == "rock" and player == "scissors") or (computer == "paper" and player == "rock") or (computer == "scissors" and player == "paper"):
    print("Computer wins!")
else:
    print("You wins!")