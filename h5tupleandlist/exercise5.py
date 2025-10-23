numbers = [42,18,17,0,2,19,0]
print(numbers)

for i in range(len(numbers)-1):
    if numbers[i] == 0:
        largest_od = numbers[i]
        for j in range(i + 1, len(numbers)):
            if numbers[j] % 2 != 0 and numbers[j] > largest_od:
                largest_od = numbers[j]
        numbers[i] = largest_od
print(numbers)