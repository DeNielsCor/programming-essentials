input_file = open('Files Chapter 7/exercise10.txt')
output_file = open('exercise11_result.py','w')

lines = input_file.readlines()
for line in lines:
    output_file.write(line[5:])

output_file.close()
input_file.close()