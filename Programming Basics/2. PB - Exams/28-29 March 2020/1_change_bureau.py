# Read User's Input
bitcoin_amount = int(input())
cny_amount = float(input())
commission = float(input())

# Logic
bitcoin_to_bgn = bitcoin_amount * 1168
cny_to_usd = cny_amount * 15 / 100
cny_to_bgn = cny_to_usd * 1.76
bgn = bitcoin_to_bgn + cny_to_bgn
euro = bgn / 1.95
euro = euro - euro * commission / 100

# Print Output
print(f"{euro:.2f}")
