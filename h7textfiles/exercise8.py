with open('Files Chapter 7/contacts.csv') as file:
    boys = []
    girls = []
    lines = file.readlines()
    print(lines)

    for line in lines:
        record = line.split(';')
        if record[3].__contains__("V"):
            girls.append((record[1], record[0]))
    girls.sort()
    girls = [f"{first} {last}" for first, last in girls]

    for line in lines:
        record = line.split(';')
        if record[3].__contains__("M"):
            boys.append((record[1], record[0]))
    boys.sort()
    boys = [f"{first} {last}" for first, last in boys]

    print(f"{len(girls)} girls:")
    for girl in girls:
        print(f"\t {girl}")

    print(f"{len(boys)} boys:")
    for boy in boys:
        print(f"\t {boy}")