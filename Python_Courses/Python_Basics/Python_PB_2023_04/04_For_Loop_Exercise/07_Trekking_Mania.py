mussala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

climbers_groups_count = int(input())
for _ in range(climbers_groups_count):
    current_climbers = int(input())

    if current_climbers < 6:
        mussala_count += current_climbers
    elif current_climbers < 13:
        monblan_count += current_climbers
    elif current_climbers < 26:
        kilimanjaro_count += current_climbers
    elif current_climbers < 41:
        k2_count += current_climbers
    elif current_climbers >= 41:
        everest_count += current_climbers

total_climbers = mussala_count + monblan_count + kilimanjaro_count + k2_count + everest_count

mussala_percent = mussala_count / total_climbers * 100
monblan_percent = monblan_count / total_climbers * 100
kilimanjaro_percent = kilimanjaro_count / total_climbers * 100
k2_percent = k2_count / total_climbers * 100
everest_percent = everest_count / total_climbers * 100

print(f"{mussala_percent :.2f}%")
print(f"{monblan_percent :.2f}%")
print(f"{kilimanjaro_percent :.2f}%")
print(f"{k2_percent :.2f}%")
print(f"{everest_percent :.2f}%")
