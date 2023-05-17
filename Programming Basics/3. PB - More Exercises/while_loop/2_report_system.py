# Data Input
expected_amount = int(input())
price = input()

# Logic
flag = True
price_integer = int(price)
payment_counter = 0
current_amount = 0
cash_amount = 0
card_amount = 0
cash_counter = 0
card_counter = 0
average_payment_in_cash = 0
average_payment_in_card = 0
while price != "End":
    payment_counter += 1
    if payment_counter % 2 != 0:
        if price_integer > 100:
            print("Error in transaction!")
        else:
            cash_counter += 1
            cash_amount += price_integer
            current_amount += price_integer
            print("Product sold!")
    else:
        if price_integer < 10:
            print("Error in transaction!")
        else:
            card_counter += 1
            card_amount += price_integer
            current_amount += price_integer
            print("Product sold!")
    if current_amount >= expected_amount:
        average_payment_in_cash += cash_amount / cash_counter
        average_payment_in_card += card_amount / card_counter
        print(f"Average CS: {average_payment_in_cash:.2f}")
        print(f"Average CC: {average_payment_in_card:.2f}")
        break
    price = input()
    if price == "End":
        flag = False
        continue
    else:
        price_integer = int(price)

# Print Output
if not flag:
    print("Failed to collect required money for charity.")
