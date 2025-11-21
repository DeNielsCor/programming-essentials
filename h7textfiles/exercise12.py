from random import randint

number = randint(1, 10)
table = []

with open(f'Files Chapter 7/table_{number}.txt', 'w') as file:
    for i in range(1,11):
        result = i * number
        print(f"{i}x{number}={result}")
        table.append(f"{i}x{number}={result}\n")
    file.writelines(table)