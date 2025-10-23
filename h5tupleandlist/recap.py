fruits = ["apple", "banana", "cherry", "date", "pear"]

print(f"{fruits[1]}")
print(f"{fruits[-1]}")

animal_names = ['cat', 'dog', 'mouse', 'rat', 'squirrel', 'owl', 'rabbit']

print("Original list:\t\t", animal_names)

animals = animal_names[-2:] + animal_names[2:-2] + animal_names[0:2]
print("After switching: \t", animals)

letters = []

text= input("Enter a text: ").lower()
vowels = 'aeiou'
for i in range(len(text)):
    if text[i] in vowels and not text[i] in letters:
        letters.append(text[i])
    print(*letters)