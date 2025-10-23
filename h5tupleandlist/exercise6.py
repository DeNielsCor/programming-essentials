text = str(input("Fill in text: "))
letters = []
letters.extend(list(text))
for letter in text:
    if letter != ' ' and letter not in letters:
        letters.append(letter)
        letters.sort()
print(letters)
print(*letters)
print(*letters, sep="\t")
