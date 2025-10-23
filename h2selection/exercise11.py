weight = float(input("Your weight in kilograms: "))
length = float(input("Your length in centimetres: "))

bmi_calculator = weight / length**2 * 10000

print("A person of " + str(weight) + " kg with a length of " + str(length) + " cm has a BMI of " + str(bmi_calculator))

if bmi_calculator < 18:
    result = "underweight"
elif 18 <= bmi_calculator < 25:
    result = "normal weight"
elif 25 <= bmi_calculator < 27:
    result = "slighty overweight"
elif 27 <= bmi_calculator < 30:
    result = "moderate overweight"
elif 30 <= bmi_calculator < 40:
    result = "obese"
elif 40 <= bmi_calculator:
    result = "sickly obese"
else:
    print("Something went wrong.")
print("This is a " + result + ".")