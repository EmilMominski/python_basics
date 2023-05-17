# Read User's Input
budget = float(input())
n = int(input())

# Logic
total_price = 0
for _ in range(n):
    title = input()
    price = float(input())
    if title == "Thrones":
        price = price - price * 50 / 100
    elif title == "Lucifer":
        price = price - price * 40 / 100
    elif title == "Protector":
        price = price - price * 30 / 100
    elif title == "TotalDrama":
        price = price - price * 20 / 100
    elif title == "Area":
        price = price - price * 10 / 100
    total_price += price
difference = abs(budget - total_price)

# Print Output
if budget >= total_price:
    print(f"You bought all the series and left with {difference:.2f} lv.")
else:
    print(f"You need {difference:.2f} lv. more to buy the series!")
