number = int(input("Enter a number: "))
last_digit = number % 10

if number < 0:
    print("Negative numbers will not be tested.")
else:
    test_number = int(input("What final digit do you want to test with: "))
    if test_number == last_digit:
        print(str(number) + " ends with " + str(test_number))
    else:
        print(str(number) + " does not end with " + str(test_number))