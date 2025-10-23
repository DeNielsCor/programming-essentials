text = str(input("Enter a text: "))

largest_block = 0
previous_letter = ""
current_block = 1

for letter in text:
    if letter == previous_letter:
        current_block += 1
    else:
        previous_letter = letter
        current_block = 1
    if current_block > largest_block:
        largest_block = current_block
print(f"The length of the largest block in this text is {largest_block}")