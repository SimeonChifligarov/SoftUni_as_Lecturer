target_book = input()  # e.g. 'Troy'

books_checked = 0
# 1. init
command = input()  # 'No More Books', OR current_book e.g. 'Stronger'
# 2. check condition
while command != 'No More Books':
    current_book = command
    # books_checked += 1

    if current_book == target_book:
        break

    books_checked += 1

    command = input()  # 3. potential change


if current_book == target_book:
    # print(f'You checked {books_checked - 1} books and found it.')
    print(f'You checked {books_checked} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {books_checked} books.')
