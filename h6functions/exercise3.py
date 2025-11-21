def password_checker(password):
    correct = "This password is ok!"
    incorrect = "This password does not meet the criteria"
    longer_than_12 = False

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z']
    capital_letters = []
    for letter in letters:
        capital_letters.append(letter.upper())
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    punctuations = ['!', '#', '$', '%', '&', '@']

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_punctuation = False

    if len(password) >= 12:
        longer_than_12 = True

    for letter in password:
        if letter in capital_letters:
            has_uppercase = True
        elif letter in letters:
            has_lowercase = True
        elif letter in digits:
            has_digit = True
        elif letter in punctuations:
            has_punctuation = True

    if longer_than_12 and has_uppercase and has_lowercase and has_digit and has_punctuation:
        print(correct)
        return correct
    else:
        print(incorrect)
        return incorrect

assert(password_checker('8&tSD%EmKke$8rs#')) == "This password is ok!"
assert(password_checker('agP#9Y0fUo%i')) == "This password is ok!"
assert(password_checker('2v$tqj&x$&1qN4ZYgk')) == "This password is ok!"
assert(password_checker('kENb#lv77')) == "This password does not meet the criteria"
assert(password_checker('770xbi#&!n3e')) == "This password does not meet the criteria"
assert(password_checker('vfJLD!Nt#Ul')) == "This password does not meet the criteria"

password = str(input("Please provide a password to check: "))
password_checker(password)