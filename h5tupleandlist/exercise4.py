tuple = (1, 2, 3, 4, 6, 7, 8)
index = 0

if 4 not in tuple:
    print("The number 4 does not appear in the Tuple")
else:
    print(tuple)
    for i in range(len(tuple)):
        if tuple[i] == 4:
            index = i
    print(tuple[index + 1:])