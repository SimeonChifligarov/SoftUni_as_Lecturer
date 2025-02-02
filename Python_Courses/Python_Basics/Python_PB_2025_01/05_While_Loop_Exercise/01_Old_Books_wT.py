target_book = input()

books_checked = 0
while True:
    command = input()  # 'No More Books' or current_book, e.g. 'Stronger'

    if command == 'No More Books':
        break

    current_book = command  # NOT another input()

    if current_book == target_book:
        break

    books_checked += 1

if command == 'No More Books':
    print('The book you search is not here!')
    print(f'You checked {books_checked} books.')
else:
    print(f'You checked {books_checked} books and found it.')
