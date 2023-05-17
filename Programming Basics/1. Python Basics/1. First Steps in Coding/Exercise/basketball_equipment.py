annual_fee = int(input())
shoes = annual_fee - (annual_fee * 40 / 100)
clothing = shoes - (shoes * 20 / 100)
ball = clothing / 4
accessories = ball / 5
total_price = annual_fee + shoes + clothing + ball + accessories
print(total_price)
