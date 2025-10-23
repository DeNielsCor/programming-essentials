text = str(input("Enter a word: "))
if "in" in text:
    if "in" in text[0:2]:
        print("'in' appears in the first or second place")
    elif "in" in text[1:3]:
        print("'in' appears in the first or second place")
    else:
        print("'in' appears in the word, but not in front")
else:
    print("this word does not contain 'in'")