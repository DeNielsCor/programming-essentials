voted_yes = int(input("How many people voted YES: "))
voted_no = int(input("How many people voted NO: "))
voted_blank = int(input("Number of blank votes: "))

total_votes = voted_yes + voted_no + voted_blank
percentage_yes = voted_yes / total_votes * 100
percentage_no = voted_no / total_votes * 100
percentage_blank = voted_blank / total_votes * 100

print("YES: " + str(percentage_yes) + "%")
print("NO: " + str(percentage_no) + "%")
print("BLANK: " + str(percentage_blank) + "%")