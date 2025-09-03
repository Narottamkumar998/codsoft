import random

# simple rock-paper-scissors game
def computer_turn():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def check_winner(user, comp):
    if user == comp:
        return "draw"
    elif (user == "rock" and comp == "scissors") or \
         (user == "scissors" and comp == "paper") or \
         (user == "paper" and comp == "rock"):
        return "user"
    else:
        return "comp"

def main():
    user_score = 0
    comp_score = 0
    round_no = 1

    print("Welcome to Rock Paper Scissors Game")
    print("Rules: Rock > Scissors, Scissors > Paper, Paper > Rock")

    while True:
        print(f"\nRound {round_no}")
        user_choice = input("Choose rock / paper / scissors: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, try again.")
            continue

        comp_choice = computer_turn()
        print("You picked:", user_choice)
        print("Computer picked:", comp_choice)

        result = check_winner(user_choice, comp_choice)

        if result == "draw":
            print("It's a tie.")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            comp_score += 1

        print("Score -> You:", user_score, "| Computer:", comp_score)

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("\nFinal Score -> You:", user_score, "| Computer:", comp_score)
            if user_score > comp_score:
                print("Congrats, you win the game!")
            elif comp_score > user_score:
                print("Computer wins the game.")
            else:
                print("Match ended in a tie.")
            break

        round_no += 1

# start game
main()
