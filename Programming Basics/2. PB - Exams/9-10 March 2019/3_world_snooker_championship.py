# Data Input
stage = input()    # Quarterfinal, Semi final and Final
ticket_type = input()    # Standard, Premium and VIP
ticket_amount = int(input())
trophy = input()    # Y or N

# Logic
flag = True
single_ticket_price = 0
if stage == "Quarter final":
    if ticket_type == "Standard":
        single_ticket_price += 55.5
    elif ticket_type == "Premium":
        single_ticket_price += 105.2
    elif ticket_type == "VIP":
        single_ticket_price += 118.9
elif stage == "Semi final":
    if ticket_type == "Standard":
        single_ticket_price += 75.88
    elif ticket_type == "Premium":
        single_ticket_price += 125.22
    elif ticket_type == "VIP":
        single_ticket_price += 300.4
elif stage == "Final":
    if ticket_type == "Standard":
        single_ticket_price += 110.1
    elif ticket_type == "Premium":
        single_ticket_price += 160.66
    elif ticket_type == "VIP":
        single_ticket_price += 400
total_price = single_ticket_price * ticket_amount

if 2500 < total_price <= 4000:
    total_price -= total_price * 10 / 100
elif total_price > 4000:
    flag = False
    total_price -= total_price * 25 / 100
if trophy == "Y":
    if flag:
        total_price += ticket_amount * 40

# Print Output
print(f"{total_price:.2f}")