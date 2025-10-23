width = float(input("Width: "))
breadth = float(input("Breadth: "))
desired_length = 2 * (width + breadth)
poles_amount = desired_length / 3
print("You need " + str(desired_length) + " metres of wire and " + str(poles_amount) + " poles.")