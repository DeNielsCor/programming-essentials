year = int(input("Enter a year: "))

if year <= 1582:
    if year % 4 == 0:
        print("This is a leap year.")
    else:
        print("This is not a leap year.")
else:
    if year % 4000 == 0:
        print("This is not a leap year.")
    elif year % 100 == 0:
        print("This is not a leap year.")
    elif year % 400 == 0:
        print("This is a leap year.")
    elif year % 4 == 0:
        print("This is a leap year.")
    else:
        print("This is not a valid year.")