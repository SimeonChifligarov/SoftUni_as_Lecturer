NO_MORE_BOOKS_COMMAND = "No More Books"

checked_books_count = 0
target_book = input()

while True:
    current_command = input()  # current_book OR "No More Books"
    if current_command == NO_MORE_BOOKS_COMMAND:
        print("The book you search is not here!")
        print(f"You checked {checked_books_count} books.")
        break

    checked_books_count += 1

    current_book = current_command
    if current_book == target_book:
        checked_books_count -= 1
        print(f"You checked {checked_books_count} books and found it.")
        break
