import random

# Ask user for their input/choice

print("Let's play Rock, Paper, Scissors!")

player_score = 0
computer_score = 0
keep_playing = True

while keep_playing is True:
    player_choice = input("What do you choose?: ")  # r, R, rock , Rock

    # Make a random choice for the computer

    computer_options = ["rock", "paper", "scissors"]

    computer_choice = random.choice(computer_options)

    # print(computer_choice)

    # Allow user input match/mesh with computer random choice

    if player_choice[0].lower() == "r":
        player_choice = "rock"
    elif player_choice[0].lower() == "p":
        player_choice = "paper"
    elif player_choice[0].lower() == "s":
        player_choice = "scissors"
    else:
        print("Not a valid answer. Do you want to quit?")

    if player_choice is "rock" and computer_choice is "paper":
        print("Computer chose Paper - Player loses")
        computer_score += 1
    elif player_choice == computer_choice:
        print("This round is a tie")
    # elif player_choice is "rock" and computer_choice is "rock":
    #     print("Computer chose Rock as well - This round is a tie")
    elif player_choice is "rock" and computer_choice is "scissors":
        print("Computer chose Scissors - Player wins this round")
        player_score += 1
    elif player_choice is "paper" and computer_choice is "scissors":
        print("Computer chose Scissors - Player loses")
        computer_score += 1
    # elif player_choice is "paper" and computer_choice is "paper":
        # print("Computer chose Paper as well - This round is a tie")
    elif player_choice is "paper" and computer_choice is "rock":
        print("Computer chose Rock - Player wins this round")
        player_score += 1
    elif player_choice is "scissors" and computer_choice is "rock":
        print("Computer chose Rock - Player loses")
        computer_score += 1
    # elif player_choice is "scissors" and computer_choice is "scissors":
        # print("Computer chose Scissors as well - This round is a tie")
    elif player_choice is "scissors" and computer_choice is "paper":
        print("Computer chose Paper - Player wins this round")
        player_score += 1

    print("The score is {} : {}".format(player_score, computer_score))
    keep_playing = input("Would you like to play again?: ")
    if keep_playing[0].lower() == "n":
        print("Thank you for playing!")
        keep_playing = False
    else:
        keep_playing = True

# keep track of score

