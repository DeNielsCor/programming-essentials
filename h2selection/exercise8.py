number_wine = int(input("How many bottles of wine are there: "))
number_pizza = int(input("How many pizzas are there: "))

if 5 < number_wine >= number_pizza * 2 or 5 < number_pizza >= number_wine * 2:
    result = "fantastic"
elif number_wine >= 5 and number_pizza >= 5:
    result = "good"
else:
    result = "stupid"
print("This is a " + result + " party")