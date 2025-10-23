number = -1
i = 0
total = 1

while number != 0:
    number = int(input("Enter a number, stop by entering a zero: "))
    if number == 0:
        break
    i += 1
    total *= number

print("The product of the " +str(i) + " number(s) is " + str(total))