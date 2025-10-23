number = int(input("Enter a three-digit number: "))

half = number / 2
print("Half = " + str(half))

double = number * 2
print("Double = " + str(double))

third_power = number ** 3
print("Third power = " + str(third_power))

tenfold = number * 10
print("Tenfold = " + str(tenfold))

first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10
print("The digits are: \n" + str(first_digit) + "\n" + str(second_digit) + "\n" + str(third_digit))