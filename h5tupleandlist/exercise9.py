print("Enter your name and the distance to school.\nType stop when you want to close the entry.")
Names = []
Distances = []

while True:
    name = str(input("Your name: "))
    if name.lower() == "stop":
        break
    else:
        distance = float(input("Distance to school: "))
        Names.append(name)
        Distances.append(distance)

average_distance = sum(Distances) / len(Distances)

if len(Names) != 0:
    print("Overview")
    for i in range(len(Names)):
        print(f'{Names[i]} {Distances[i]}')
    max = max(Distances)
    print(f"{Names[Distances.index(max)]} lives farthest, namely {max} km")
    print(f"The average distance is {average_distance:.2f}")