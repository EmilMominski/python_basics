nylon_cover = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
nylon_cover_price = (nylon_cover + 2) * 1.5
paint_price = (paint + paint * 10 / 100) * 14.5
thinner_price = thinner * 5
bag_price = 0.4
price_for_supplies = nylon_cover_price + paint_price + thinner_price + bag_price
payment_per_hour = price_for_supplies * 30 / 100
hours_of_work_payment = payment_per_hour * hours
total_price = price_for_supplies + hours_of_work_payment
print(total_price)
