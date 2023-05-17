# Read User Input
fruit = input()
day = input()
quantity = float(input())
fruit_price = 0

# Logic
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or \
        day == "Thursday" or day == "Friday":
    if fruit == "banana":
        fruit_price = 2.5
    elif fruit == "apple":
        fruit_price = 1.2
    elif fruit == "orange":
        fruit_price = 0.85
    elif fruit == "grapefruit":
        fruit_price = 1.45
    elif fruit == "kiwi":
        fruit_price = 2.7
    elif fruit == "pineapple":
        fruit_price = 5.5
    elif fruit == "grapes":
        fruit_price = 3.85
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        fruit_price = 2.7
    elif fruit == "apple":
        fruit_price = 1.25
    elif fruit == "orange":
        fruit_price = 0.9
    elif fruit == "grapefruit":
        fruit_price = 1.6
    elif fruit == "kiwi":
        fruit_price = 3.0
    elif fruit == "pineapple":
        fruit_price = 5.6
    elif fruit == "grapes":
        fruit_price = 4.20

price = fruit_price * quantity

# Print Output
if price != 0:
    print(f"{price:.2f}")
else:
    print("error")
