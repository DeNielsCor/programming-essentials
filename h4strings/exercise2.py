word = str(input("Enter a word: "))
number = int(input("Enter a number: "))
make_word = word[0] + (word[-number::1])
print(make_word)