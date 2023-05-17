# Read User's Input
days = int(input())
room_type = input()      # room for one person; apartment; president apartment
appraisal = input()        # positive or negative

# Logic
price = 0
nights = days - 1
if room_type == "room for one person":
    price = nights * 18
elif room_type == "apartment":
    price = nights * 25
    if days < 10:
        price -= price * 30 / 100
    elif 10 <= days <= 15:
        price -= price * 35 / 100
    elif days > 15:
        price -= price * 50 / 100
elif room_type == "president apartment":
    price = nights * 35
    if days < 10:
        price -= price * 10 / 100
    elif 10 <= days <= 15:
        price -= price * 15 / 100
    elif days > 15:
        price -= price * 20 / 100
if appraisal == "positive":
    price += price * 25 / 100
elif appraisal == "negative":
    price -= price * 10 / 100

# Print Output
print(f"{price:.2f}")
