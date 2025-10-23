input_text = str(input("Enter a string: "))
output_text = ""
i = 0

while i < len(input_text):
    group = input_text[i:i+3]
    if len(group) == 3:
        output_text += group[1:] + group[0]
    else:
        output_text += group
    i += 3
print(output_text)

# n = 3
# arrayofthrees = [input_text[i:i+n] for i in range(0, len(input_text), n)]
# for i in arrayofthrees:
#     if len(i) == 3:
#         print(i[1] +i[2] + i[0], end="")
#     else:
#         print(i, end="")