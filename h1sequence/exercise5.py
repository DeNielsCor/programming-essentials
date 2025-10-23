exchange_rate = float(input("Enter the current exchange dollar rate (€-> $): "))
amount = float(input("Enter your amount in euro: "))
exchange_amount = exchange_rate * amount
print(str(amount) + " € = " + str(exchange_amount) + " $")