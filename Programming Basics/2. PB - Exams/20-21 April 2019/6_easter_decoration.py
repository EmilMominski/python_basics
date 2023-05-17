customers_count = int(input())

total_price = 0
for i in range(customers_count):
    price = 0
    item_count = 0
    while True:
        purchase_type = input()     # basket, wreath or chocolate bunny
        if purchase_type == "Finish":
            if item_count % 2 == 0:
                price -= price * 20 / 100
            print(f"You purchased {item_count} items for {price:.2f} leva.")
            break
        if purchase_type == "basket":
            price += 1.5
        elif purchase_type == "wreath":
            price += 3.8
        elif purchase_type == "chocolate bunny":
            price += 7
        item_count += 1
    total_price += price
average_price = total_price / customers_count

print(f"Average bill per client is: {average_price:.2f} leva.")
