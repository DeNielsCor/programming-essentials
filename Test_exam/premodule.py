#r1075317 Corstiaans Niels 1ITF05
# Geen breaks en while True
minimum = int(input('Enter the minimum value: '))
maximum = int(input('Enter the maximum value: '))

user_input = input('Enter a number, stop by entering Q: ')
number_list = []

while user_input.upper() != 'Q':
    if minimum <= int(user_input) <= maximum:
        number_list.append(int(user_input))
    else:
        print(f'Enter a number between {minimum} and {maximum} please!')

    user_input = input('Enter a number, stop by entering Q: ')

count_list = []
for i in range(maximum - minimum + 1):
    count_list.append(0)

for user_input in number_list:
    count_list[user_input - minimum] += 1

for i in range(len(count_list)):
    print(f"{i + minimum} {count_list[i]}")


# minimum = int(input("Enter a minimum number: "))
# maximum = int(input("Enter a maximum number: "))
# numbers = 0
# List = []
#
# while True:
#     user_input = input("Enter a number, stop by entering Q: ")
#
#     if user_input.lower() == 'q':
#         break
#     else:
#         number = int(user_input)
#     if number < minimum or number > maximum:
#         print(f"Enter a number between {minimum} and {maximum} please!")
#     else:
#         numbers += 1
#         List.append(number)
#
# print(f"\nYou have entered {numbers} valid numbers")
# print(f"\nAn overview of the numbers")
#
# for i in range(minimum, maximum + 1):
#     count = List.count(i)
#     print(f"{i} {count}")