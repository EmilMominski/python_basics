deposit_string = ""
total_sum = 0
while True:
    deposit_string = input()
    if deposit_string != "NoMoreMoney":
        deposit_digit = float(deposit_string)
        if deposit_digit >= 0:
            print(f"Increase: {deposit_digit:.2f}")
            total_sum = total_sum + deposit_digit
        else:
            print("Invalid operation!")
            break
    else:
        break
print(f"Total: {total_sum:.2f}")
