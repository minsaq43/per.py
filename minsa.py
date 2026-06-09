import random

while True:
  user_choice = input("Rock , paper or scissors? (r/p/s): ").lower()
  choices = ("r","p" , "s")
 
  if user_choice not in choices :
    print("Invalid choice!")
    continue
  computer_choice = random.choice(choices)
  emojis = {"r":"🪨","s":"✂","p":"📃"}
  print(f"Your choice{emojis[user_choice]}")
  print(f"Computer chose{emojis[computer_choice]}")
  if user_choice == computer_choice:
    print("Tie!")
  elif (user_choice == "r" and computer_choice == "s" ) or (user_choice == "s" and computer_choice =="p") or (user_choice == "p" and computer_choice == "r"):
   print("Your win!")
  else:
   print("You lose!")
  should_continue = input("Continue? (y/n): ").lower()
  if should_continue == "n" :
   break
 