z_counter = 0
line_amount = 1

with open('Files Chapter 7/first_names.txt') as file:

    line = file.readline()

    for line in file:
        line_amount += 1
        name = line.strip()



        if 'z' in name.lower():
            z_counter += 1
            print(name)

    print(f"There are {line_amount} first names in the file.")
    print(f"{z_counter} of which contain a letter z.")
file.close()