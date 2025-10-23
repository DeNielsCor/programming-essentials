number = int(input("Enter a number: "))

List = []

for i in range(1 , 11):
    for y in range(1, number + 1):
        solutions = i * y
        List.append(solutions)
        print(str(solutions), i, end=" ----- ")