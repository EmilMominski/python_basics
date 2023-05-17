city = input()      # Bansko, Borovets, Varna, or Burgas
extras = input()        # noEquipment, withEquipment, noBreakfast, or withBreakfast
vip_discount = input()      # yes or no
days = int(input())

price = 0
flag = True
if days < 1:
    print("Days must be positive number!")
else:
    if city == "Bansko" or city == "Borovets":
        if extras == "noEquipment":
            if vip_discount == "yes":
                price = 80 - 80 * 5 / 100
            elif vip_discount == "no":
                price = 80
        elif extras == "withEquipment":
            if vip_discount == "yes":
                price = 100 - 100 * 10 / 100
            elif vip_discount == "no":
                price = 100
        else:
            flag = False
    elif city == "Varna" or city == "Burgas":
        if extras == "noBreakfast":
            if vip_discount == "yes":
                price = 100 - 100 * 7 / 100
            elif vip_discount == "no":
                price = 100
        elif extras == "withBreakfast":
            if vip_discount == "yes":
                price = 130 - 130 * 12 / 100
            elif vip_discount == "no":
                price = 130
        else:
            flag = False
    else:
        flag = False
    if days > 7:
        total_price = price * (days - 1)
    else:
        total_price = price * days

    if flag:
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
    else:
        print("Invalid input!")
