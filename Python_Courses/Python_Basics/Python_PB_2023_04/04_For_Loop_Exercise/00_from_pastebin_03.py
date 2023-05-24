# Step 1 we start by collecting the user input and define the variables for doctors and patients
period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

# Step 2 lets start the for loop
for period in range(1, period + 1):
    patients_per_day = int(input())
    if period % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if patients_per_day <= doctors:
        treated_patients += patients_per_day
    else:
        treated_patients += doctors
        untreated_patients += (patients_per_day - doctors)

# Step 3 we print the result
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
