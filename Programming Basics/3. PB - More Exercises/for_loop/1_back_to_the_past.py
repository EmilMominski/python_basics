# Data Input
inherited_money = float(input())
year = int(input())

# Logic
flag = True
remaining_money = inherited_money
money_needed = 0
for i in range(1800, year + 1):
    if i % 2 == 0:
        remaining_money -= 12000
    elif i % 2 != 0:
        remaining_money -= 12000 + 50 * (18 + (i - 1800))
if remaining_money < 0:
    flag = False
    money_needed += abs(remaining_money)

# Print Output
if flag:
    print(f"Yes! He will live a carefree life and will have {remaining_money:.2f} dollars left.")
else:
    print(f"He will need {money_needed:.2f} dollars to survive.")
