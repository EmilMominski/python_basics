# Data Input
beginning_digit = int(input())
end_digit = int(input())
magic_digit = int(input())

# Logic and Print Output
counter = 0
sum_i_j = int()
for i in range(beginning_digit, end_digit + 1):
    for j in range(beginning_digit, end_digit + 1):
        counter += 1
        sum_i_j = i + j
        if sum_i_j == magic_digit:
            print(f"Combination N:{counter} ({i} + {j} = {sum_i_j})")
            break
    if sum_i_j == magic_digit:
        break
else:
    print(f"{counter} combinations - neither equals {magic_digit}")
