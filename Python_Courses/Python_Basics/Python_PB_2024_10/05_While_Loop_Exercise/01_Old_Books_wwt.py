target_book = input()

book_checked = 0
while True:
    command = input()  # 'No More Books' or current_book as a string

    if command == 'No More Books':
        break

    current_book = command
    if current_book == target_book:
        break

    book_checked += 1


if command == 'No More Books':
    print('The book you search is not here!')
    print(f'You checked {book_checked} books.')
else:
    print(f'You checked {book_checked} books and found it.')
