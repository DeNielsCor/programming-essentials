#example 1
#1: open file
file = open('Files Chapter 7/schedule.txt')

#2: read and display full content file
print(file.read())

totale_file = file.read()
print(type(totale_file))
print(totale_file)

#3: close file
#moet niet in python, doet dit by default
file.close()

#example 2
#1: open file
with open('Files Chapter 7/schedule.txt') as file:

    #2: read line by line
    line = file.readline() #priming read

    while line:
        if line != '\n':
            print(line.rstrip()) # haalt de whitespaces weg
        line = file.readline() #read next

#3: close file
print()
file.close()

#example 3
# 1: open file
with open('Files Chapter 7/schedule.txt') as file:

# 2: read line by line
    line = file.readline()

    while line:
        if line != '\n':
            record = line.split(';')
            #print(record)
            #print(record[0])
            #print(record[1])
            #print(record[2])
            print(f"{record[0]} {record[1]} {record[2].rstrip()}")
        line = file.readline()

#3: close file
print()
file.close()

#example 4
with open('Files Chapter 7/kilometers.txt') as file:
    line = file.readline().rstrip()
    smallest = largest = int(line)

    line = file.readline().rstrip()
    while line:
        number = int(line)
        if number > largest:
            largest = number
        else:
            if number < smallest:
                smallest = number
        line = file.readline().rstrip()

difference = largest - smallest
print('The difference between the largest and the smallest number =',
largest, '-', smallest, '=', difference)

print()
file.close()

#example 5
with open('Files Chapter 7/schedule.txt') as file:
    # read all lines and place them in a list of strings
    all_lines = file.readlines()
    file.close()

    for line in all_lines:
        if line != '\n':
            print(line, end='')
print("\n")

#example 6
with open('Files Chapter 7/schedule.txt') as file:
    all_lines = file.readlines()
    file.close()
    print(all_lines)

    for line in all_lines:
        if line != '\n':
            # line is split into record of fields
            record = line.split(';')
            print(record[0], record[2].rstrip(), record[1], sep='\t')

#Part 2
#1 Open file
file = open('schedule.txt', 'w')

#2 Write data to file
file.write('25/11;Bob Potters; 08:30')
file.write('30/11;René François; 12:30')
file.write('02/12;Chris Benz; 10:15')

#3 Close file
file.close()
