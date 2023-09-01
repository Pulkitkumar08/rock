import random
def get_player_choice():
    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"]);
    
