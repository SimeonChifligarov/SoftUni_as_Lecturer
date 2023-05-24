days = int(input())
current_day = 0
doctors_qty = 7
untreated_per_day = 0
all_untreated = 0
all_patients = 0

for day in range(1, days + 1):
    patients_qty = int(input())
    current_day += 1


    if current_day % 3 == 0:
        if all_untreated > all_patients - all_untreated:
            doctors_qty += 1

    all_patients += patients_qty

    if patients_qty > doctors_qty:
        untreated_per_day = patients_qty - doctors_qty
    else:
        untreated_per_day = 0

    all_untreated += untreated_per_day
treated_patients = all_patients - all_untreated

print(f'Treated patients: {treated_patients}.\nUntreated patients: {all_untreated}.')