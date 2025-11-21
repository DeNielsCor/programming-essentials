with open('Files Chapter 7/irish_song.txt') as file:
    line = shortest_line = file.readline()
    while line:
        if len(line.rstrip()) < len(shortest_line.rstrip()):
            shortest_line = line
        line = file.readline().rstrip()

print(f'The shortest line has {len(shortest_line)} characters')
print(shortest_line)

file.close()