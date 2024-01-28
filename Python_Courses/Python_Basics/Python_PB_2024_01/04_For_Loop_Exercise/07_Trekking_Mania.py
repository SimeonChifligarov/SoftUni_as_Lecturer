mussala_count = 0
monblanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

groups_count = int(input())

for _ in range(groups_count):
    climbers_count = int(input())
    if climbers_count <= 5:
        mussala_count += climbers_count
    elif climbers_count <= 12:
        monblanc_count += climbers_count
    elif climbers_count <= 25:
        kilimanjaro_count += climbers_count
    elif climbers_count <= 40:
        k2_count += climbers_count
    elif climbers_count >= 41:
        everest_count += climbers_count

climbers_total_count = mussala_count + monblanc_count + kilimanjaro_count + k2_count + everest_count
mussala_percent = mussala_count / climbers_total_count * 100
monblan_percent = monblanc_count / climbers_total_count * 100
kilimanjaro_percent = kilimanjaro_count / climbers_total_count * 100
k2_percent = k2_count / climbers_total_count * 100
everest_percent = everest_count / climbers_total_count * 100

print(f"{mussala_percent :.2f}%")
print(f"{monblan_percent :.2f}%")
print(f"{kilimanjaro_percent :.2f}%")
print(f"{k2_percent :.2f}%")
print(f"{everest_percent :.2f}%")
