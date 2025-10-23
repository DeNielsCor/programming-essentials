i = 0
List = []
divisible_by_3 = 0

while i != 10:
    number = int(input("Enter a number: "))
    i += 1
    List.append(number)

    if number % 3 == 0:
        divisible_by_3 += 1

print("The largest number is " + str(max(List)) + ", the smallest is " + str(min(List))
    + " and the amount of numbers divisible by 3 are: " + str(divisible_by_3))