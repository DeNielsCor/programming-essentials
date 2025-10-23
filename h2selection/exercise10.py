first_number = int(input("First number: "))
second_number = int(input("Second number: "))

List = [65, 72, 83, 90]

if 40 >= first_number >= 30 and 40 >= second_number >= 30:
    print("Both numbers are ok")
elif first_number in List and second_number in List:
    print("Both numbers are ok")
else:
    print("They are NOT ok")