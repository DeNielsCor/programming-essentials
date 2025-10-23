first_number = int(input("First number: "))
second_number = int(input("Second number: "))

list = [first_number, second_number]

if first_number < 0 or second_number < 0:
    first_number = abs(first_number)
    second_number = abs(second_number)

if first_number % 5 == 0 < second_number:
    result = abs(min(list))
elif second_number % 5 == 0 < first_number:
    result = abs(min(list))
elif first_number > second_number:
    result = max(list)
elif second_number > first_number:
    result = max(list)
elif second_number == first_number:
    result = 0

print("The answer for the number " + str(first_number) + " and " + str(second_number) +
          " is " + str(result) + ".")