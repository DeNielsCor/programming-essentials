print("Enter the scores for the test. Use -1 if you want to finish")
Scores = []

while True:
    number = float(input("score: "))
    if number != -1:
        Scores.append(number)
    else:
        break

average = sum(Scores) / len(Scores)
Scores.sort()
print(f"The scores (ordered): {Scores}")
print(f"The average of these {len(Scores)} scores = {average:.2f}")