import string

input_file = open('Files Chapter 7/hamlet.txt')
output_file = open('Files Chapter 7/hamlet2.txt', 'w')

punctuation_marks = list(string.punctuation)
lines = input_file.readlines()



output_file.close()
input_file.close()