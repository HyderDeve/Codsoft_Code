import random

def play_game():
    user_choice=input("Enter Your Choice (rock/paper/scissors): ").lower()
    choices=["rock","paper","scissors"]
    computer_choice=random.choice(choices)
    print(f"Your Chose {user_choice}")
    print(f"\nComputer Chose {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You Win!" if computer_choice == "scissors" else "Computer Wins!"
    elif user_choice == "paper":
        return "You Win!" if computer_choice == "rock" else "Computer Wins!"
    elif user_choice == "scissors":
        return "You Win!" if computer_choice == "paper" else "Computer Wins!"
    else:
        return "Invalid input. Please Choose rock, paper, or scissors."


while(True):
    result= play_game()
    print(result)
    cont=input("\nDo you want to continue? Yes/No").lower()
    if cont=="yes":
        continue
    elif(cont=="no"):
        break
