chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())
chicken_menu_price = chicken_menu_count * 10.35
fish_menu_price = fish_menu_count * 12.4
vegetarian_menu_price = vegetarian_menu_count * 8.15
total_menu_price = chicken_menu_price + fish_menu_price + \
                   vegetarian_menu_price
dessert = total_menu_price * 20 / 100
total_price = total_menu_price + dessert + 2.5
print(total_price)
