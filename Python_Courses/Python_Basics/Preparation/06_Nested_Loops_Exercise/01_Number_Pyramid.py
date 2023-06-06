last_number = int(input())

current = 1
is_current_bigger = False
for row in range(1, last_number + 1):
    for col in range(1, row + 1):
        if current > last_number:
            is_current_bigger = True
            break

        print(f"{current} ", end="")
        current += 1

    if is_current_bigger:
        break
    print()
