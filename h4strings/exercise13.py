while True:
    name = str(input("Your name (press enter to stop): "))
    if name == "":
        break

    print("\nMenu:")
    print("*****")
    print("U uppercase \nL lowercase \nA alternative")

    even_character = []
    odd_character = []

    choice = str(input("Make a choice (U-L-A): "))

    while True:
        if choice == "U" or choice == "u":
            print(name.upper() + "\n")
            break
        elif choice == "L" or choice == "l":
            print(name.lower() + "\n")
            break
        elif choice == "A" or choice == "a":
            result = ""
            for i, char in enumerate(name):
                if i % 2 == 0:
                    result += char.upper()
                else:
                    result += char.lower()
            print(result)
            break
        else:
            choice = str(input("Make a choice (U-L-A): "))