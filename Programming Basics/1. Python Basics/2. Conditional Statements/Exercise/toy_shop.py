price_of_excursion = float(input())
puzzles = int(input())
speaking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

toys_ordered = puzzles + speaking_dolls + teddy_bears + minions + trucks
puzzles_sold = puzzles * 2.6
speaking_dolls_sold = speaking_dolls * 3
teddy_bears_sold = teddy_bears * 4.1
minions_sold = minions * 8.2
trucks_sold = trucks * 2
total_sold = puzzles_sold + speaking_dolls_sold + teddy_bears_sold + \
             minions_sold + trucks_sold

if toys_ordered >= 50:
    discount = total_sold * 25 / 100
    total_sold = total_sold - discount

rent = total_sold * 10 / 100
profit = total_sold - rent
remaining_money = abs(profit - price_of_excursion)

if profit >= price_of_excursion:
    print("Yes! " f"{remaining_money:.2f} " "lv left.")
else:
    print("Not enough money! " f"{remaining_money:.2f} " "lv needed.")
