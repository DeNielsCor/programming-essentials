with open('Files Chapter 7/first_names.txt') as file:
    first_names = file.readlines()
    counter = 0
    for name in first_names:
        print(name.rstrip().ljust(13), end="")
        counter += 1
        if counter % 10 == 0:
            print()

file.close()