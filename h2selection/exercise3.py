first_number = int(input("Number 1: "))
second_number = int(input("Number 2: "))
third_number = int(input("Number 3: "))

List = [first_number, second_number, third_number]
print("The smallest number is " + str(min(List)))

# if first_number < second_number and first_number < third_number:
#     print("The smallest number is " + str(first_number))
# elif second_number < first_number and second_number < third_number:
#     print("The smallest number is " + str(second_number))
# else:
#     print("The smallest number is " + str(third_number))

#DOCENT CODE
# smallest = first_number
#
# if second_number < smallest:
#     smallest = second_number
# if third_number < smallest:
#     smallest = second_number
#
# print("The smallest number is " + str(smallest))