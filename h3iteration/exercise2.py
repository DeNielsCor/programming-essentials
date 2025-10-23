number = int(input("Enter a number: "))
zero = 0
six = 0
last_digit = number % 10

# while number > 0:

for digit in str(last_digit):
    if digit == "0":
        zero += 1
    if digit == "6":
        six += 1
print("The number consists of " + str(zero) + " zeros and " + str(six) + " sixes")