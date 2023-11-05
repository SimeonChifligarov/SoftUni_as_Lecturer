# print('it works')

# budget = 0
# while budget < 1000:  # vacation_cost = 1000
#     print('I am saving 150...')
#     budget += 150
#
# print(f"Yes, I am going to vacation with 1000 cost, because I saved {budget}")

# money_needed = 1000
# should_break = False
# budget = 0
# for day in range(1, 6):   # [1, 2, 3, 4, 5]
#     print(f"=> I am working day - {day}")
#     for hour in range(1, 9):  # [1, 2, 3, 4, 5, 6, 7, 8]
#         if hour == 5:
#             print(f"Hour {hour} - I am taking a break")
#             continue
#         print(f"--- I am working hour - {hour}; still day is {day}")
#         budget += 150
#
#         if budget >= 1000:
#             should_break = True
#             break
#
#     if should_break:
#         break
#
# print('---')
# print(budget)

# print('line 1')
# print()  # print('') end='\n'
# print('line 2')

# my_name = 'Simo'
# print(my_name[0])
# print(my_name[1])
# print(my_name[2])

# int("stop")

# number = int(input())
#
# is_prime = True
# for n in range(2, number):  # [2, 3, ..., number - 1]
#     if number % n == 0:  # 3 % 1 == 0; 3 % 3 == 0
#         is_prime = False
#         break
#
#
# if is_prime:
#     print(f"{number} is prime")
# else:
#     print(f"{number} is not prime")
# number = 1
#
# for num in range(2, number):  # range(2, 1) => []
#     print('here')
#     print(num)

# number = 10
# 10 % 2 == 0 -> is_prime = False
# 10 % 3 == 0
# 10 % 4 == 0
# 10 % 5 == 0

# for n in range(1_111, 9_999):
#     # check if n is_special
#     # if special -> print
#     print(f"{n} ", end="")

# num = int(input())
#
# num_as_string = str(num)


# for _, digit in enumerate("4911"):
#     # print(f"idx hold {idx}; digit hold {digit}")
#     print(f"digit - {digit}")  # "4", "9"
#     print(type(digit))

# print(3 // 0)

# for num in range(10):
#     print(num)

# for digit in "4123":
#     print(digit)
# n = 3
# is_special = True
# for _, digit in enumerate("1100"):  # n -> 1_111, ..., 9_999
#     digit_as_int = int(digit)  # int("1") == 1
#
#     if digit_as_int == 0:
#         continue
#
#     if n % digit_as_int != 0:
#         is_special = False
#         break
#
# if is_special:
#     print(f"{n} ", end="")


# print(ord("a"))
# print(ord("A"))
# print(ord("b"))
# print(ord("c"))
# ASCII

# print(chr(97))
# print(chr(65))
# print(chr(98))
# print(chr(99))
