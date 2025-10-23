first_number = int(input("number 1 (0, 1 or 2): "))
second_number = int(input("number 2 (0, 1 or 2): "))
third_number = int(input("number 3 (0, 1 or 2): "))

if first_number == 2 and second_number == 2 and third_number == 2:
    result = "10"
elif first_number == second_number == third_number and first_number != 2 and second_number != 2 and third_number != 2:
    result = "5"
elif second_number != first_number and third_number != first_number:
    Result = "1"
else:
    result = "0"
print(result)