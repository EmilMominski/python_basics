budget = float(input())
participants = int(input())
price_per_participant = float(input())

decor = budget * 10 / 100
price_for_clothing = participants * price_per_participant
discount = price_for_clothing * 10 / 100

if participants >= 150:
    price_for_clothing = price_for_clothing - discount

expenses = decor + price_for_clothing
remaining_money = abs(expenses - budget)

if expenses <= budget:
    print("Action!")
    print("Wingard starts filming with " f"{remaining_money:.2f} " 
          "leva left.")
elif expenses > budget:
    print("Not enough money!")
    print("Wingard needs " f"{remaining_money:.2f} " "leva more.")
