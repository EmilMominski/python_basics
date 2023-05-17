contract_duration = input()     # one or two
contract_type = input()     # Small, Middle, Large or ExtraLarge
mobile_internet = input()       # yes or no
months_to_pay = int(input())

price = 0
if contract_duration == "one":
    if contract_type == "Small":
        price += 9.98
    elif contract_type == "Middle":
        price += 18.99
    elif contract_type == "Large":
        price += 25.98
    elif contract_type == "ExtraLarge":
        price += 35.99
elif contract_duration == "two":
    if contract_type == "Small":
        price += 8.58
    elif contract_type == "Middle":
        price += 17.09
    elif contract_type == "Large":
        price += 23.59
    elif contract_type == "ExtraLarge":
        price += 31.79

if mobile_internet == "yes":
    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85
elif mobile_internet == "no":
    price = price

price *= months_to_pay
if contract_duration == "two":
    price -= price * 3.75 / 100

print(f"{price:.2f} lv.")
