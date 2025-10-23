first_name = str(input("Enter the first name: "))
second_name = str(input("Enter the second name: "))
print("Before changing: " + first_name + " " + second_name)

help = first_name
first_name = second_name
second_name = help

print("After changing: " + first_name + " " + second_name)