def celsius_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    print(f'{celsius} degrees Celsius = {fahrenheit} degrees Fahrenheit')
    return fahrenheit

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    print(f'{fahrenheit} degrees Fahrenheit = {celsius} degrees Celsius')
    return celsius

assert celsius_fahrenheit(38) == 100.4
assert celsius_fahrenheit(39) == 102.2
assert celsius_fahrenheit(39.3) == 102.74
assert celsius_fahrenheit(40.7) == 105.26

assert fahrenheit_celsius(99.5) == 37.5
assert fahrenheit_celsius(101.3) == 38.5
assert fahrenheit_celsius(104) == 40
assert fahrenheit_celsius(107.6) == 42

options = ['c', 'f']
question_answer = str(input('Do you want to convert starting from Celsius (enter C) or Fahrenheit (enter F): '))

while question_answer.lower() in options:
    if question_answer.lower() == 'c':
        celsius = float(input('Degrees: '))
        celsius_fahrenheit(celsius)
        question_answer = str(input('Do you want to convert starting from Celsius (enter C) or Fahrenheit (enter F): '))
    if question_answer.lower() == 'f':
        fahrenheit = float(input('Degrees: '))
        fahrenheit_celsius(fahrenheit)
        question_answer = str(input('Do you want to convert starting from Celsius (enter C) or Fahrenheit (enter F): '))