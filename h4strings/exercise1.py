colour = str(input("What is your favorite colour: "))

print(f"{colour[0]}{colour[2]}")

print(f"This colour consists of {len(colour)} letters\n")

for letter in colour:
    print(letter + ' = ', ord(letter))
print("")
count = 0
test = 0
while count < len(colour):
    if test == 0:
        print(f"##{colour[count]}##")
    else:
        print(f"**{colour[count]}**")
    count += 1
    test = count % 2