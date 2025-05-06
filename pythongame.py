import random

user_score = 0
computer_score = 0

def game_rules():
    global user_score, computer_score, user_choice, computer_choice
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1




while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        continue
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    game_rules()  # Apply the game rules using the choices

    print(f"Score -> You: {user_score}, Computer: {computer_score}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break