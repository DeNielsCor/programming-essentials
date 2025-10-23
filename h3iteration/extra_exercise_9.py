guess_count = 1

player_choice = int(input("Enter a positive number for the computer to guess: "))

low = 0
high = 1000

while True:
    computer_choice = (low + high) // 2 # smarter than the random randint

    print("Enter a positive number: " + str(computer_choice))

    feedback = input("Is it too high (H), too low (L), or correct (C) ")

    if feedback == "H":
        low = computer_choice - 1
    elif feedback == "L":
        high = computer_choice + 1
    elif feedback == "C":
        print("You have guessed the number " +
              str(player_choice) + " in " + str(guess_count) + " turns.")
        break
    else:
        print("Not a valid input, please type H, L or C ")
    guess_count += 1