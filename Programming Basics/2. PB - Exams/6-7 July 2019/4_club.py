# Read User's Input
expected_profit = float(input())
cocktail = input()
cocktail_amount = int(input())

# Logic
real_profit = 0
while cocktail != "Party!":
    cocktail_price = len(cocktail)
    all_cocktails_price = cocktail_price * cocktail_amount
    if all_cocktails_price % 2 != 0:
        all_cocktails_price = all_cocktails_price - all_cocktails_price * 25 / 100
    real_profit += all_cocktails_price
    if real_profit >= expected_profit:
        print("Target acquired.")
        break
    cocktail = input()
    if cocktail == "Party!":
        print(f"We need {abs(real_profit - expected_profit):.2f} leva more.")
        continue
    cocktail_amount = int(input())

# Print Output
print(f"Club income - {real_profit:.2f} leva.")
