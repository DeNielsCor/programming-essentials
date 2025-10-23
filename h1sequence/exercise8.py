current_hour = int(input("Enter the current hour: "))
sleep = int(input("How long do you want to sleep: "))
total = current_hour + sleep
time = total % 24
print("The alarm will sound at: " + str(time) + "h.")