numbers = number = 10
while number >= 10 and number <= 20:
    while number > -1:
        print(number, end =" ")
        number -= 1
    number = (number + numbers + 3)
    numbers += 2
    print("\n")