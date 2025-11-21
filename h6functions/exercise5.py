import random
import string


def password_structure(structurelength):
    password_list = []
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    punctuation = ['!', '#', '$', '%', '&']
    digit = list(string.digits)
    test = lower_case + upper_case + punctuation + digit

    if structurelength < 4:
        structurelength = 4
        print("Password that will be generated, will have minimum length of 4")

    while len(password_list) != structurelength:
        password_list.append(random.choice(test))

    print(test)
    print(password_list)
    return password_list

amount_password = int(input("How many passwords do you want to generate: "))
length_password = int(input("What should the length be: "))

password_structure(length_password)