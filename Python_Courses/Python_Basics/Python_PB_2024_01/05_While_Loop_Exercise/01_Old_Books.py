target_book = input()  # e.g. "Troy"

counter = 0
is_book_found = False
command = input()  # either current_book, either command "No More Books"  # 1.
while command != "No More Books":  # 2.
    book = command

    if book == target_book:
        is_book_found = True
        break
    counter += 1

    command = input()  # 3.

if is_book_found:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
