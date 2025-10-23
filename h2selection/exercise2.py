year = int(input("Enter your year of birth: "))
age = 2025 - year

print("Your age = " + str(age))

if age < 18:
    print("You're not an adult yet.")
else:
    print("So you're an adult.")