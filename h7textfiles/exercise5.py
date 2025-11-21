with open('Files Chapter 7/books.txt') as file:
    counter = 1
    book = file.readline().rstrip()
    while book:
        author = file.readline().rstrip()
        print(f'{counter}. {book} -> {author}')
        counter +=1
        book = file.readline().rstrip()

file.close()