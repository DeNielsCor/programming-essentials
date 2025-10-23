import random

player_chose = ""
tie_count = 0
user_count = 0
computer_count = 0
# print("You chose " + player_chose)
#
# print("I chose " + computer) # computer chose

# if computer == player_chose:
#     print("It's a tie.")
# elif (player_chose == "rock" and computer == "scissors"
#       or player_chose == "scissors" and computer == "paper"
#       or player_chose == "paper" and computer == "rock"):
#     print("You win :-)")
# else:
#     print("Computer wins :-(")

while True:
    List = ["rock", "paper", "scissors"]
    computer = random.choice(List)

    player_chose = str(input("What do you choose: paper, rock or scissors? Type stop to stop. "))

    if player_chose == "stop":
        print("Thanks for playing!")
        print("Ties: " + str(tie_count) +
              "\nPlayer wins: " + str(user_count) +
              "\nComputer wins: " + str(computer_count))
        break

    print("You chose " + player_chose)
    print("I chose " + computer)  # computer chose
    match player_chose, computer:
        case (player_chose, computer) if player_chose not in List:
            print("Invalid option. Please choose rock, paper or scissors.")
        case (player_chose, computer) if player_chose == computer:
            result = "It's a tie."
            tie_count += 1
        case ("rock" , "scissors") | ("scissors", "paper") | ("paper", "rock"):
            result = "You win :-)"
            user_count += 1
        case _:
            result = "Computer wins :-("
            computer_count += 1
    print(result)