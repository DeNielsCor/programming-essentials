number = -1
List = []

while number != 0:
    number = int(input("Enter a number: "))
    if number == 0:
        if not List:
            print("No numbers entered")
            break
        List.append(number)
        sum_of_numbers = int(abs(max(List))) + int(abs(min(List)))
        print("The difference between the largest number " + str(max(List))
              + " and the smallest " + str(min(List)) + " = " + str(sum_of_numbers))
        break