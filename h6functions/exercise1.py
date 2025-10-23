def convertEuroToDollar(amount_euro, exchange_rate):
    exchanged = amount_euro * exchange_rate
    print(f"€ {amount_euro} = $ {exchanged}")
    return exchanged

assert convertEuroToDollar(965, 1.2327) == 1189.5555
assert convertEuroToDollar(200, 1.1234) == 224.67999999999998
assert convertEuroToDollar(350, 1.4321) == 501.23499999999996

rate = float(input("Current dollar rate (€ -> $): "))
euro = int(input("Your amount in Euro: "))

convertEuroToDollar(euro, rate)