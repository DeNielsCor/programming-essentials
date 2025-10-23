text = input("What do you eat for lunch: ")

first_position = text.find('sandwich')

if first_position != -1:
    part_text = text[first_position + 8:]
    second_position = part_text.find('sandwich')
    if second_position != -1:
        print("You have", part_text[0:second_position],"between your sandwich")