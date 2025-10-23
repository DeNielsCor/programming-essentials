# STEP OVER f8
weight = int(input("Your weight in kilograms: "))
length = int(input("Your length in centimetres: "))

bmi = weight / (length / 100) ** 2

if bmi < 18:
    result = "underweight"
elif bmi < 25:
    result = "normal weight"
elif bmi < 27:
    result = "slightly overweight"
elif bmi < 30:
    result = "moderate overweight"
elif bmi < 40:
    result = "obese"
else:
    result = "sickly obese"

print("A person of", str(weight), "with a length of", str(length), "cm has as BMI", str(bmi))
print("This is", result, ".")