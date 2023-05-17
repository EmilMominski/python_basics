# Data Input
season = input()    # Spring, Summer, Autumn or Winter
kilometers_per_month = float(input())

# Logic
coefficient = 0
if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        coefficient += 0.75
    elif season == "Summer":
        coefficient += 0.9
    elif season == "Winter":
        coefficient += 1.05
elif 5000 < kilometers_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        coefficient += 0.95
    elif season == "Summer":
        coefficient += 1.1
    elif season == "Winter":
        coefficient += 1.25
elif 10000 < kilometers_per_month <= 20000:
    coefficient += 1.45
salary = kilometers_per_month * coefficient * 4
salary -= salary * 10 / 100

# Print Output
print(f"{salary:.2f}")
