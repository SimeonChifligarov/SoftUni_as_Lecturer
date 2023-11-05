start = int(input())
end = int(input())

list_start = list(map(int, str(start)))
list_end = list(map(int, str(end)))

for num in range(start, end + 1):
    is_the_one = True
    for index, digit in enumerate(str(num)):
        digit = int(digit)
        if digit in range(int(list_start[index]), int(list_end[index]) + 1):
            if digit % 2 == 0:
                is_the_one = False
                break
        else:
            is_the_one = False
            break

    if is_the_one:
        print(num, end=" ")
