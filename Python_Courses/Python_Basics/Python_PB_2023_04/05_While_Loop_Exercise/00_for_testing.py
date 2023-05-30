# # print('it works!')
#
# # for ...
# #
# # while ...
#
# print('here')
# # break
#
# # for i in range(5):
# #     print(i)
# #     if i == 3:
# #         continue
# #
# #     print('some action')
#
#
# # digit = input("Insert your digit here: ")
# # while digit != "9":
# #     print('your input is ok')
# #     if digit == "3":
# #         print('Will continue..')
# #         digit = input("Insert your digit here: ")
# #         continue
# #
# #     print('end if not continued')
# #     digit = input("Insert your digit here: ")
#
# # while True:
# #     digit = input("Insert your digit here: ")
# #     print('will print every time')
# #
# #     if digit == "3":
# #         continue
# #
# #     print('not cont...')
#
# # while True:
# #     print("while True")
#
# # # Solution 1
# # checked_books = 0
# # target_book = input()
# #
# #
# # command = input()
# # while command != "No More Books":
# #     current_book = command
# #     if current_book == target_book:
# #         break
# #
# #     checked_books += 1
# #     command = input()
# #
# # if command != "No More Books":
# #     print(f"You checked {checked_books} books and found it.")
# # else:
# #     print("The book you search is not here!")
# #     print(f"You checked {checked_books} books.")
# #
# # # Solution 2
# # NO_MORE_BOOKS_COMMAND = "No More Books"
# #
# # checked_books = 0
# # target_book = input()
# #
# # command = input()
# # while not command == NO_MORE_BOOKS_COMMAND:
# #     current_book = command
# #     if current_book == target_book:
# #         print(f"You checked {checked_books} books and found it.")
# #         break
# #
# #     checked_books += 1
# #     command = input()
# # else:
# #     print("The book you search is not here!")
# #     print(f"You checked {checked_books} books.")
# #
#
# # Solution 3
# NO_MORE_BOOKS_COMMAND = "No More Books"
#
# checked_books = 0
# target_book = input()
#
# is_book_found = False
# while True:
#     command = input()
#     if command == NO_MORE_BOOKS_COMMAND:
#         break
#
#     current_book = command
#     if current_book == target_book:
#         is_book_found = True
#         break
#
#     checked_books += 1
#
#
# if is_book_found:
#     print(f"You checked {checked_books} books and found it.")
# else:
#     print("The book you search is not here!")
#     print(f"You checked {checked_books} books.")
#
# money_need = 550
# current_money = 100
#
# total_money = current_money
# for _ in range(2):
#     total_money += 155
#     if total_money >= money_need:
#         print("I am going to the vacation!")
#         break
#
#
# # else:
# #     print("I am not going")
# # if total_money < money_need:
# #     print("I am not going")

# command = input()
# while command != "Stop":
#     print('YESSS')
#     print(command)
#
#     command = input()
#
# print("here")
# print(command)

# for i in range(5):  # for-else; [0, 1, 2, 3, 4]
#     print(i)
#
# print(i)

# # 1
#
# some_condition
# while some_condition != "End":
#     some_logic_here()
#
#     some_condition  # change value here
#
# # 2
# some_condition
# while some_condition != "End":
#     some_logic_here()
#
#     if some_other_condition:
#         break
#
#     some_condition  # change value here
#
#
# # 3
# while True:
#     some_condition
#     some_logic_here()
#
#     if some_other_condition:
#         break
#
# # EXTRA
# # including the boolean variable improves code readability
# is_failed = False
# while ...:
#
#     if ...:
#         is_failed = True
#         break
#
# if not is_failed:
#     print("")
# else:
#     print("")

# num1 = 0.1 + 0.2
# num2 = 0.3
#
# print(num1 == num2)
# print(num1)
# print(num2)
# print(2.49 * 100)

# print(int("Going home"))  # ValueError: invalid literal for int() with base 10: 'Going home'


# while condition:  # do-while


# do... ...
#
# while ...:
#
#
# import sys
#
# print('print this')
# outside_variable = sys.argv[1]
# print(outside_variable)

# print(10_000_222)
# print(2e-2)
