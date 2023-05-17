# Read User's Input
shirt_price = float(input())
ball_sum = float(input())

# Logic
shorts_price = shirt_price * 75 / 100
socks_price = shorts_price * 20 / 100
shoes_price = (shirt_price + shorts_price) * 2
price_without_discount = shirt_price + shorts_price + socks_price + shoes_price
price_after_discount = price_without_discount - price_without_discount * 15 / 100

# Print Output
if price_after_discount >= ball_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {price_after_discount:.2f} lv.")
else:
    difference = abs(price_after_discount - ball_sum)
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")
