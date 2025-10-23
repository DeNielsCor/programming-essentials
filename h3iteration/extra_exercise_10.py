number = int(input("Enter a number: "))
result = True

if number <= 1:
    print(str(number) + " is not a prime number.")
else:
    for i in range(2, number):

        if number % i == 0:
            result = False
            break
    if result:
        print(str(number) + " is a prime number.")
    else:
        print(str(number) + " is not a prime number.")
