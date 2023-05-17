budget = float(input())
gpu = int(input())
cpu = int(input())
ram = int(input())

price_gpu = gpu * 250
price_cpu = cpu * price_gpu * 35 / 100
price_ram = ram * price_gpu * 10 / 100
total_price = price_gpu + price_cpu + price_ram

if gpu > cpu:
    discount = total_price * 15 / 100
    total_price = total_price - discount

difference = abs(total_price - budget)

if total_price <= budget:
    print("You have " f"{difference:.2f} " "leva left!")
elif total_price > budget:
    print("Not enough money! You need " f"{difference:.2f} " "leva more!")
