import random

computer_choice = random.randint(0, 1000)

guess_count = 1

while True:
    player_choice = int(input("Enter a positive number: "))

    if player_choice == computer_choice:
        print("You have guessed the number " +
              str(computer_choice) + " in " + str(guess_count) + " turns.")
        break

    if player_choice < computer_choice:
        result = "Higher!"
    elif player_choice > computer_choice:
        result = "Lower!"
    print(result)
    guess_count += 1