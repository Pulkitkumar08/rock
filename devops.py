import random
def get_player_choice():
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        mode = input("Choose a mode (computer vs. computer, computer vs. player, player vs. player, or quit): ").lower()
        if mode == "quit":
            break
        elif mode == "computer vs. computer":
            computer1_choice = get_computer_choice()
            computer2_choice = get_computer_choice()
            print(f"Computer 1 chose {computer1_choice}.")
            print(f"Computer 2 chose {computer2_choice}.")
            print(determine_winner(computer1_choice, computer2_choice))
if _name_ == "_main_":
    main()
