import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    # comp selects one item randomly from the list
    computer_choice = random.choice(options)
    # store both in a dictionary
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    # printing using formatted output 
    print(f"You chose {player}, computer chose {computer}")
    
    
    if player == computer:
        return "It's a tie!"
    
    # Nested loop for conditions  to evaluate wether win/loss states
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
            
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
            
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
