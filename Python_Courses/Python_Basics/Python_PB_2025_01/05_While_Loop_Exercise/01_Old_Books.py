target_book = input()  # e.g. 'Troy'

books_checked = 0
is_book_found = False

command = input()  # 'No More Books' or book, e.g. 'Stronger'
while command != 'No More Books':
    current_book = command  # e.g. 'Stronger'

    if current_book == target_book:
        is_book_found = True
        break

    books_checked += 1

    command = input()


if not is_book_found:
    print('The book you search is not here!')
    print(f'You checked {books_checked} books.')
else:
    print(f'You checked {books_checked} books and found it.')
