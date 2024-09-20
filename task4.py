import random
user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("You lose!")

def play_game():
    global user_score, computer_score
    
    while True:
        print("\nChoose rock, paper, or scissors:")
        user_choice = input().lower()
        
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        result = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, result)
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        
        print(f"\nScores: You {user_score} - Computer {computer_score}")
        
        print("\nDo you want to play again? (yes/no)")
        play_again = input().lower()
        
        if play_again != "yes":
            print("Thanks for playing!")
            break
play_game()
