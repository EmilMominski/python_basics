# Data Input
budget = float(input())
category = input()    # VIP or Normal
people_in_the_group = int(input())

# Logic
transport_budget = 0
ticket_price = 0
if 1 <= people_in_the_group <= 4:
    transport_budget += budget * 75 / 100
elif 5 <= people_in_the_group <= 9:
    transport_budget += budget * 60 / 100
elif 10 <= people_in_the_group <= 24:
    transport_budget += budget * 50 / 100
elif 25 <= people_in_the_group <= 49:
    transport_budget += budget * 40 / 100
elif people_in_the_group >= 50:
    transport_budget += budget * 25 / 100
if category == "VIP":
    ticket_price += 499.99
elif category == "Normal":
    ticket_price += 249.99
total_ticket_expenses = people_in_the_group * ticket_price
total_expenses = total_ticket_expenses + transport_budget
difference = abs(budget - total_expenses)

# Print Output
if total_expenses <= budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
