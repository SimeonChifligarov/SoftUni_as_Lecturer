target_book = input()  # <class 'str'>  # Troy

book_checked = 0
is_book_found = False
# 1. init
command = input()  # book (e.g. 'Stronger'), or 'No More Books'
# 2. check
while command != 'No More Books':
    book = command  # 'Stronger'

    if book == target_book:
        is_book_found = True
        break

    book_checked += 1

    # 3. change
    command = input()

# if command == 'No More Books':
#     print('The book you search is not here!')
#     print(f'You checked {book_checked} books.')
# else:
#     print(f'You checked {book_checked} books and found it.')

if is_book_found:
    print(f'You checked {book_checked} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {book_checked} books.')
