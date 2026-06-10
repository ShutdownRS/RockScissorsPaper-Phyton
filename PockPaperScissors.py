import random

print("Welcome to the rock paper scissors game!")
while True:
    print("\nChoose: rock, scissors or paper")
    player_choice = input("Your choice: ").lower()
    if player_choice not in ["rock", "scissors", "paper"]:
        print("Error! write: rock, paper, or scissors")
        continue
    result = random.choice(["win", "lose"])
    if result == "win":
        print("You win!")
    else:
        print("You loose!")
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for game! Goodbye!")
        break 
