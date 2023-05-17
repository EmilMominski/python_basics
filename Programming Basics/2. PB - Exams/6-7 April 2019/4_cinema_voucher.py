# Data Input
voucher_value = int(input())
purchase = input()

# Logic
voucher_amount = voucher_value
tickets_amount = 0
purchases_amount = 0

while purchase != "End":
    length_purchase = len(purchase)
    flag = False
    if length_purchase > 8:
        purchase_price = ord(purchase[0]) + ord(purchase[1])
        flag = True
    else:
        purchase_price = ord(purchase[0])
    voucher_amount -= purchase_price
    if voucher_amount < 0:
        break
    else:
        if flag:
            tickets_amount += 1
        else:
            purchases_amount += 1
        if voucher_amount == 0:
            break
        purchase = input()

# Output
print(tickets_amount)
print(purchases_amount)


