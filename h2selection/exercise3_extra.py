letter = str(input("Enter a letter: "))
vowels = ["a", "e", "i", "o", "u"]

if letter in vowels:
    print("vowel")
elif letter == "y":
    print("exception")
else:
    print("consonant")