power_consumption_during_day = int(input("Power consumption during the day (kilowatt per hour): "))
power_consumption_at_night = int(input("Power consumption at night (kilowatt per hour): "))
fixed_cost = 83.6
daily_consumption = power_consumption_during_day * 0.146
night_consumption = power_consumption_at_night * 0.073
total_excluding_vat = fixed_cost + daily_consumption + night_consumption
total_including_vat = total_excluding_vat * 1.06

print("Invoice")
print("*" * 7)
print("Fixed costs: €" + str(fixed_cost))
print("Daily consumption: €" + str(daily_consumption))
print("Night consumption: €" + str(night_consumption))
print("Total excluding VAT: €" + str(total_excluding_vat))
print("Total including VAT: €" + str(total_including_vat))