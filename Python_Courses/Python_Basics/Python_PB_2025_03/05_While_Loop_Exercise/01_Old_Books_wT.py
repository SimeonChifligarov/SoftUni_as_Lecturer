target_book = input()  # e.g. 'Troy'

is_book_found = False
books_checked = 0
while True:
    command = input()  # 'No More Books', or current_book e.g. 'Stronger'

    if command == 'No More Books':
        break

    current_book = command

    if current_book == target_book:
        is_book_found = True
        break

    books_checked += 1

if is_book_found:
    print(f'You checked {books_checked} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {books_checked} books.')
