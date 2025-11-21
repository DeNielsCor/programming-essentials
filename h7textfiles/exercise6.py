from random import randint

random_number = randint(1, 10)

with open(f'Files Chapter 7/wish{random_number}.txt') as file:
    print(f"Wish {random_number}\n  \n{file.read()}")

file.close()