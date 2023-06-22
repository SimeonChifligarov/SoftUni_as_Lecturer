result = []

last_sector = input()
rows_first_count = int(input())
seats_odd_count = int(input())

current_rows = rows_first_count
for s in range(ord("A"), ord(last_sector) + 1):
    current_sector = chr(s)
    for c_r in range(1, current_rows + 1):
        if c_r % 2 == 0:
            current_seats = seats_odd_count + 2
        else:
            current_seats = seats_odd_count

        for c_s in range(1, current_seats + 1):
            current_seat = chr(c_s + 96)
            result_str = f"{current_sector}{c_r}{current_seat}"
            result.append(result_str)

    current_rows += 1

print("\n".join(result))
print(len(result))
