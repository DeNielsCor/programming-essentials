text = str(input("Enter a text: "))
previous_letter = ""
count = 1
triple_count = 0

for letter in text:
    if letter == previous_letter:
        count += 1
    else:
        count = 1
        previous_letter = letter
    if count == 3:
        triple_count += 1

if triple_count == 1:
    print(f"There is {triple_count} triple in this text")
elif triple_count > 1:
    print(f"There are {triple_count} triples in this text")
else:
    print("There are no triples in this text")