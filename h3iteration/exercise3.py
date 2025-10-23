your_age = int(input("How old are you: "))
father_age = int(input("How old is your father: "))
year = 0

if father_age / 2 < your_age:
    print("The situation is no longer possible for your ages.")
elif father_age / 2 == your_age:
    print("You are currently in this situation.")
else:
    while father_age / 2 != your_age:
        year += 1
        father_age += 1
        your_age += 1
    else:
        print("Within " + str(year) + " years your father will be twice your age")
        print("Your father will be " + str(father_age) + " and you will be " + str(your_age) + ".")