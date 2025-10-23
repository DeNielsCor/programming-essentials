text = input("Enter a text: ")
every_x_followed_by_y = True

for letter in range(len(text)):
    if text[letter] == 'x':
        if 'y' not in text[letter + 1:]:
            every_x_followed_by_y = False
            break

if every_x_followed_by_y:
    result = "every x is followed by y."
else:
    result = "not every x is followed by a y."
print("In this text", result)