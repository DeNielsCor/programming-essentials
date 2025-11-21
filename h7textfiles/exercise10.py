input_file = open('age_father_son.py')
output_file = open('Files Chapter 7/exercise10.txt','w')

lines = input_file.readlines()
line_number = 1
for line in lines:
    output_file.write(str(line_number).rjust(4) + ' ' + line)
    line_number += 1

output_file.close()
input_file.close()