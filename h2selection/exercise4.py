first_number = int(input("number 1: "))
second_number = int(input("number 2: "))
third_number = int(input("number 3: "))

List = [first_number,second_number,third_number]

max_number = max(List)

List.remove(max_number)

if List[0]+List[1] == max_number:
    print("this works")
else:
    print("this doesn't work")