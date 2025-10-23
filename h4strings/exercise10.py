word_1 = str(input("Enter word 1: "))
word_2 = str(input("Enter word 2: "))
word_3 = str(input("Enter word 3: "))
word_4 = str(input("Enter word 4: "))
word_5 = str(input("Enter word 5: "))

word = [word_1.capitalize(), word_2.capitalize(), word_3.capitalize(), word_4.capitalize(), word_5.capitalize()]

print(f"The word in reverse order")
print(" ".join(word[::-1]))