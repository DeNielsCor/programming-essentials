max_temp = []

with open('Files Chapter 7/weather_2024_08.csv') as file:
    line = file.readline()
    line = file.readline()

    while line:
        line = line.split(";")
        max_temp.append(line[1])
        max_temp.sort()
        line = file.readline()

print(f"The highest temperature in this period = {max_temp[-1]} °C")
