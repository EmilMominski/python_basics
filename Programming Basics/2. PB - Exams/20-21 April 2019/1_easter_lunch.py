easter_bread_quantity = int(input())
egg_packages = int(input())
cookies_quantity = int(input())

total_bread_price = easter_bread_quantity * 3.2
total_egg_price = egg_packages * 4.35
total_cookies_price = cookies_quantity * 5.4
egg_colour_price = egg_packages * 12 * 0.15
total_price = total_bread_price + total_egg_price + total_cookies_price + egg_colour_price

print(f"{total_price:.2f}")
