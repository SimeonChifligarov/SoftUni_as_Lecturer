target_book = input()  # "Troy"
books_count = 0
is_found = False

command = input()  # "No More Books" OR f"{current_book}", e.g. "Stronger"
while command != "No More Books":

    current_book = command  # e.g. "Stronger"
    if current_book == target_book:
        is_found = True
        break

    books_count += 1
    command = input()  # here we check the next book

if not is_found:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")
else:
    print(f"You checked {books_count} books and found it.")
