members = int(input("How many members? "))
members_count = 1
fee = 0

while members_count <= members:
    print("\nInformation for member", members_count)
    members_count += 1
    name = str(input("name: "))
    age = int(input("age: "))
    membership_years = int(input("Member for how many years: "))

    if age < 12:
        fee = 20
    elif 12 >= age <= 18:
        fee = 50
    else:
        fee = 95

    if membership_years >= 5:
        fee -= fee * 0.1
    print('Member fee for', name, '=', fee)