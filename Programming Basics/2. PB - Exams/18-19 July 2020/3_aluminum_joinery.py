# Read user's Input
count = int(input())
type_product = input()      # 90X130; 100X150; 130X180; 200X300
type_delivery = input()     # With delivery or Without delivery

# Logic
price_per_piece = 0
discount = 0
flag = True

if count < 10:
    flag = False
else:
    if type_product == "90X130":
        price_per_piece += 110
        if 30 < count <= 60:
            discount += price_per_piece * 5 / 100
        elif count > 60:
            discount += price_per_piece * 8 / 100
    elif type_product == "100X150":
        price_per_piece += 140
        if 40 < count <= 80:
            discount += price_per_piece * 6 / 100
        elif count > 80:
            discount += price_per_piece * 10 / 100
    elif type_product == "130X180":
        price_per_piece += 190
        if 20 < count <= 50:
            discount += price_per_piece * 7 / 100
        elif count > 50:
            discount += price_per_piece * 12 / 100
    elif type_product == "200X300":
        price_per_piece += 250
        if 25 < count <= 50:
            discount += price_per_piece * 9 / 100
        elif count > 50:
            discount += price_per_piece * 14 / 100
final_price_per_piece = price_per_piece - discount
total = final_price_per_piece * count
if type_delivery == "With delivery":
    total += 60
elif type_delivery == "Without delivery":
    total = total
if count > 99:
    total -= total * 4 / 100

# Print Output
if flag:
    print(f"{total:.2f} BGN")
else:
    print("Invalid order")
