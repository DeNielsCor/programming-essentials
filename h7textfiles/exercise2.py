name_list = []

with open('Files Chapter 7/first_names.txt') as file:
    line = file.readline()
    while line:
        if line != '\n':
            print(line.rstrip())
            name_list.append(line.rstrip())
        line = file.readline()

    print(name_list[::-1])
file.close()