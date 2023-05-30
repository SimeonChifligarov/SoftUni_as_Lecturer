first_number = int(input())

sum_numbers = 0

while True:
    next_number = int(input())
    sum_numbers += next_number
    if sum_numbers >= first_number:
        print(sum_numbers)
        break
