# Data Input
days = int(input())

# Logic
doctors = 7
treated_patients = 0
untreated_patients = 0
for i in range(1, days + 1):
    if untreated_patients > treated_patients and i % 3 == 0:
        doctors += 1
    patients_count = int(input())
    if patients_count >= doctors:
        treated_patients += doctors
        untreated_patients += patients_count - doctors
    else:
        treated_patients += patients_count

# Print Output
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
