List = [9, 17, 25, 4, 12, 7]
New_List = []

for i in range(len(List)):
    if List[i] % 2 == 0:
        New_List.append(List[i])
for i in range(len(List)):
    if List[i] % 2 != 0:
        New_List.append(List[i])
print(List, "becomes", New_List)