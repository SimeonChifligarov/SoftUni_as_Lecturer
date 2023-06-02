stadium_capacity = int(input())
all_fans = int(input())

sector_a_count = 0
sector_b_count = 0
sector_v_count = 0
sector_g_count = 0

for _ in range(all_fans):
    current_sector = input()  # "A", "B", "V" и "G"

    if current_sector == "A":
        sector_a_count += 1
    elif current_sector == "B":
        sector_b_count += 1
    elif current_sector == "V":
        sector_v_count += 1
    elif current_sector == "G":
        sector_g_count += 1

sector_a_percent = sector_a_count / all_fans * 100
sector_b_percent = sector_b_count / all_fans * 100
sector_v_percent = sector_v_count / all_fans * 100
sector_g_percent = sector_g_count / all_fans * 100

all_fans_percent = all_fans / stadium_capacity * 100

print(f"{sector_a_percent :.2f}%")
print(f"{sector_b_percent :.2f}%")
print(f"{sector_v_percent :.2f}%")
print(f"{sector_g_percent :.2f}%")
print(f"{all_fans_percent :.2f}%")
