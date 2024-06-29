# print('while loop 😎')

# 1.
# for num in range(5):  # start=0, step=1
#     print(num)

# # 2.
# for num in range(1, 6):  # step=1
#     print(num)

# # 3
# for num in range(1, 11, 3):
#     print(num)
# import time

# for attempt in range(1, 5):
#     print(f'Attempt no: {attempt}')
#     if attempt % 2 ==0:
#         continue
#     print('  -> trying to connect to database...')
    # time.sleep(2)
    # if attempt == 3:
    #     print('Success!!!')
    #     break


# break

# for num in range(8):
#     print(num)
#     if num % 2 == 0:
#         continue
#     print('after the check')

# for i in range(5, 0):  # step=1
#     print(i)

# print('return value of func chr(i)')
# for i in range(97, 100):  # [97, 98, 99]
#     # print(chr(i))
#     print(f'  -> current value of i = {i}, and chr({i}) = {chr(i)}')
#
# print('return value of func ord(ch)')
# for ch in 'abcd':  # ['a', 'b', 'c', 'd']
#     # print(chr(i))
#     print(f'  -> current value of ch = {ch}, and ord({ch}) = {ord(ch)}')

# for num in range(0, 10, 2):
#     print(num)

# for ch in 'Simo':
#     print(ch)

# line = input()
# while line != "Stop":
#     print("Loop")
#     # line = input()
#
# print('outside while loop')

# a = 5
# while a <= 10:
#     # print("a = " + str(a))
#     print(f'a = {a}')
#     a += 1
#
# print('outside while loop')
# print(a)
# import time
#
#
# a = 1
# while True:
#     print(a)
#     a += 2
#     time.sleep(2)
#     if a >= 13:
#         break

# import time


# day = 1
#
# while day <= 100:
#     if day % 6 == 0 or day % 7 == 0:
#         day += 1
#         continue
#
#     print(f'Sending an email with day = {day}')
#     if day == 10:
#         print('User has declined our email services')
#         break
#
#     day += 1
#     time.sleep(2)

# if 'Gosho' != 'Gosho':
#     print('yes')
# else:
#     print('no')


# data = input()
# try:
#     num = int(data)
# except:
#     data = input('insert new value: ')

# if "3.56" < 0:
#     print('yes')

# 0 + '3.56'

# a = 5
# while a <= 10:
#     print(a)
#     a += 1
#     if a == 7:
#         break
#
# else:
#     print('loop ended without break')

# for num in range(1, 10):
#     print(num)
#     if num == 5:
#         break
# else:
#     print('for-loop ended without break')

# text = input()
#
# if text.isnumeric() or '.' in text:
#     print('it is numeric')
# else:
#     print('not numeric')
