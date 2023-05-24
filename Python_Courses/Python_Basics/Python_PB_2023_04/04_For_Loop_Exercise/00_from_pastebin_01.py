days = int(input())
doctors_qty = 7
all_untreated = 0
all_treated = 0

for day in range(1, days + 1):  # [1, 2, 3, ...]
    if day % 3 == 0:
        if all_untreated > all_treated:
            doctors_qty += 1

    patients_qty = int(input())

    if patients_qty > doctors_qty:
        all_treated += doctors_qty
        all_untreated += patients_qty - doctors_qty
    else:
        all_treated += patients_qty

print(f'Treated patients: {all_treated}.\nUntreated patients: {all_untreated}.')
