initial_limit = int(input("Initial limit: "))
final_limit = int(input("Final limit: "))

sum = number = initial_limit

print("Sum of numbers from " + str(initial_limit) + " till " + str(final_limit))

if initial_limit > final_limit:
    print("The initial limit must be smaller than the final limit!")
elif initial_limit == final_limit:
    # is, is niet hetzelfde als ==, is checked of 2 variabelen wijzen naar dezelfde geheugenplaats
    # als bijvoorbeeld y naar dezelfde geheugenplaats gaat als x geeft het True
    # -> is dus niet hetzelfde voor te zien of de waarden gelijk zijn
    print(number)
else:
    while number != final_limit:
        number += 1
        sum = sum + number
        print("+", number, "-->", sum)