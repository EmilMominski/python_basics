n = int(input())

flag = True
for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):
                sum_numbers = a + b + c + d
                product = a * b * c * d
                if sum_numbers == product and n % 10 == 5:
                    flag = False
                    print(f"{a}{b}{c}{d}")
                    break
                elif product // sum_numbers == 3 and n % 3 == 0:
                    flag = False
                    print(f"{d}{c}{b}{a}")
                    break
            if not flag:
                break
        if not flag:
            break
    if not flag:
        break

if flag:
    print("Nothing found")
