movie = input()     # John Wick, Star Wars, or Jumanji
extras = input()        # Drink, Popcorn, or Menu
ticket_count = int(input())

price_per_ticket = 0
if movie == "John Wick":
    if extras == "Drink":
        price_per_ticket += 12
    elif extras == "Popcorn":
        price_per_ticket += 15
    elif extras == "Menu":
        price_per_ticket += 19
elif movie == "Star Wars":
    if extras == "Drink":
        price_per_ticket += 18
    elif extras == "Popcorn":
        price_per_ticket += 25
    elif extras == "Menu":
        price_per_ticket += 30
elif movie == "Jumanji":
    if extras == "Drink":
        price_per_ticket += 9
    elif extras == "Popcorn":
        price_per_ticket += 11
    elif extras == "Menu":
        price_per_ticket += 14
price_for_all_tickets = price_per_ticket * ticket_count
if movie == "Star Wars" and ticket_count >= 4:
    price_for_all_tickets = price_for_all_tickets - price_for_all_tickets * 30 / 100
if movie == "Jumanji" and ticket_count == 2:
    price_for_all_tickets = price_for_all_tickets - price_for_all_tickets * 15 / 100

print(f"Your bill is {price_for_all_tickets:.2f} leva.")
