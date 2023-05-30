# # Solution 1
# checked_books = 0
# target_book = input()
#
#
# command = input()
# while command != "No More Books":
#     current_book = command
#     if current_book == target_book:
#         break
#
#     checked_books += 1
#     command = input()
#
# if command != "No More Books":
#     print(f"You checked {checked_books} books and found it.")
# else:
#     print("The book you search is not here!")
#     print(f"You checked {checked_books} books.")
#
# # Solution 2
# NO_MORE_BOOKS_COMMAND = "No More Books"
#
# checked_books = 0
# target_book = input()
#
# command = input()
# while not command == NO_MORE_BOOKS_COMMAND:
#     current_book = command
#     if current_book == target_book:
#         print(f"You checked {checked_books} books and found it.")
#         break
#
#     checked_books += 1
#     command = input()
# else:
#     print("The book you search is not here!")
#     print(f"You checked {checked_books} books.")
#

# Solution 3
NO_MORE_BOOKS_COMMAND = "No More Books"

checked_books = 0
target_book = input()

is_book_found = False
while True:
    command = input()
    if command == NO_MORE_BOOKS_COMMAND:
        break

    current_book = command
    if current_book == target_book:
        is_book_found = True
        break

    checked_books += 1


if is_book_found:
    print(f"You checked {checked_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")
