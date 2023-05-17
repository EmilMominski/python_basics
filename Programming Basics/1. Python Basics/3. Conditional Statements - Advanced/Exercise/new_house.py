# Read User's Input
flower = input()    # Roses, Dahlias, Tulips, Narcissus, Gladiolus
quantity = int(input())
budget = int(input())
price = 0

# Logic
if flower == "Roses":
    if quantity <= 80:
        price = quantity * 5
    elif quantity > 80:
        price = quantity * 5 - quantity * 5 * 10 / 100
elif flower == "Dahlias":
    if quantity <= 90:
        price = quantity * 3.8
    elif quantity > 90:
        price = quantity * 3.8 - quantity * 3.8 * 15 / 100
elif flower == "Tulips":
    if quantity <= 80:
        price = quantity * 2.8
    elif quantity > 80:
        price = quantity * 2.8 - quantity * 2.8 * 15 / 100
elif flower == "Narcissus":
    if quantity < 120:
        price = quantity * 3 + quantity * 3 * 15 / 100
    elif quantity >= 120:
        price = quantity * 3
elif flower == "Gladiolus":
    if quantity < 80:
        price = quantity * 2.5 + quantity * 2.5 * 20 / 100
    elif quantity >= 80:
        price = quantity * 2.5

difference = abs(price - budget)

# Print Output
if price <= budget:
    print(f"Hey, you have a great garden with {quantity} {flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
