deposit_text = input()
deposit_sum = 0

while deposit_text != "NoMoreMoney":
    deposit_digit = float(deposit_text)
    if deposit_digit < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {deposit_digit:.2f}")
        deposit_sum += deposit_digit
        deposit_text = input()

print(f"Total: {deposit_sum:.2f}")
