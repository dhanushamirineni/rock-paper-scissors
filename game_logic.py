import random

def get_bot_choice():
    """Randomly selects bot's choice."""
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    """Gets validated user choice."""
    while True:
        user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
        if user_choice in {"rock", "paper", "scissors"}:
            return user_choice
        print("Invalid input! Please choose: rock, paper, or scissors")

def play_round():
    """Plays one round and returns result message."""
    bot_choice = get_bot_choice()
    user_choice = get_user_choice()
    print(f"\nYou chose {user_choice} vs bot's {bot_choice}")
    
    if user_choice == bot_choice:
        return "It is a draw"
    elif ((user_choice == "rock" and bot_choice == "scissors") or 
          (user_choice == "paper" and bot_choice == "rock") or
          (user_choice == "scissors" and bot_choice == "paper")):
        return "You win! :)"
    return "You lose! :("

def continue_playing():
    """Checks if user wants to continue."""
    while True:
        choice = input("\nPlay again? (y/n): ").lower()
        if choice in ("y", "n"):
            return choice
        print("Invalid input! Select 'y' or 'n'.")

if __name__ == "__main__":
    wins = losses = draws = 0
    while True:
        result = play_round()
        print(result)
        
        # Update scores
        if result == "You win! :)": wins += 1
        elif result == "You lose! :(": losses += 1
        else: draws += 1
        
        print(f"Score: {wins} wins, {losses} losses, {draws} draws")
        
        if continue_playing() != "y":
            # Final message
            if wins > losses: print("\nHumans dominate every time!\n")
            elif wins < losses: print("\nRobot dominance!\n")
            else: print("\nIt's a Draw!\n")
            break