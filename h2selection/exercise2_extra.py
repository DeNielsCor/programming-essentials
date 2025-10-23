# volgens chatgpt 97 - (YYMMDDXXX mod 97)
name = str(input("Enter your name: "))
first_9_digits = str(input("Enter the first 9 digits of your national number : "))
check_digits = int(input("Enter the last 2 digits of your national number : "))

check_module_before2000 = 97 - (int(first_9_digits) % 97)
check_module_after2000 = 97 - ((2000000000 + int(first_9_digits)) % 97)

get_year = int(first_9_digits[0:2])
get_month = int(first_9_digits[2:4])
get_day = int(first_9_digits[4:6])
get_gender = int(first_9_digits[6:9])

if get_gender % 2 == 0:
    result_gender = "female"
else:
    result_gender = "male"

if check_module_before2000 == check_digits or check_module_after2000 == check_digits:
    result_cc = "correct"
else:
    result_cc = "not correct"

print("Hello " + name + ", your gender is " + result_gender + ", and the national number you gave is " + result_cc)
print("You were born on " + str(get_day) + "/" + str(get_month) + "/" + str(get_year))