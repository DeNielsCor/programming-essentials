def remove_vowels(line):
    new_line = ""
    for character in line:
        if character.lower() not in 'aeiou':
            new_line += character
    return new_line

input_file = open('Files Chapter 7/hamlet2.txt')
output_file = open("Files Chapter 7/hamlet3.txt", 'w')

number_read = 0

line = input_file.readline()
while line:
    line = input_file.readline()

output_file.close()
input_file.close()