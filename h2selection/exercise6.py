is_morning = True
is_mother = False
is_asleep = False

result = "answering"
if is_asleep or (is_morning and not is_mother):
    result = "not answering"

print("I'm " + result + " my phone.")

# te veel print statements verminderen kan met result = werken
# if is_asleep == True:
#     print("I'm not answering the phone.")
# elif is_morning == True and is_mother == False:
#     print("I'm not answering the phone.")
# else:
#     print("I'm answering the phone.")

# if is_asleep:
#     result = "not answering"
# elif is_morning and is_mother:
#     result = "answering"
# elif is_morning:
#     result = "not answering"
# else:
#     result = "answering"
#
# print("I'm " + result + " my phone.")