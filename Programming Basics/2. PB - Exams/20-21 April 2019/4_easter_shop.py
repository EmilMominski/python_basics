initial_egg_quantity = int(input())

current_egg_quantity = initial_egg_quantity
eggs_sold_counter = 0
while True:
    command = input()       # Buy or Fill
    if command == "Close":
        print("Store is closed!")
        print(f"{eggs_sold_counter} eggs sold.")
        break
    egg_purchased = int(input())
    if egg_purchased > current_egg_quantity:
        if command != "Fill":
            print("Not enough eggs in store!")
            print(f"You can buy only {current_egg_quantity}.")
            break
    if command == "Buy":
        current_egg_quantity -= egg_purchased
        eggs_sold_counter += egg_purchased
    elif command == "Fill":
        current_egg_quantity += egg_purchased
