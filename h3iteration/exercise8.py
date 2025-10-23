entries = 10
check_digit = int(input("What final digit do you want to check the numbers on: "))
correct = 0

for i in range((entries + 1) - 1):
    number = int(input("Enter a number: "))
    if number % 10 == check_digit:
        correct += 1

if correct == 1:
    print(str(correct) + " out of " + str(entries) + " numbers ends on " + str(check_digit))
else:
    print(str(correct) + " out of " + str(entries) + "numbers end on " + str(check_digit))