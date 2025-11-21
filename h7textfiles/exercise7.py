with open('Files Chapter 7/playlist.txt') as file:
    lines = file.readlines()
    lines.sort()
    print('Playlist')
    for line in lines:
        record = line.split(';')
        print(f'{record[0]} \t {record[1].upper()} ({record[2].lower().rstrip()})')