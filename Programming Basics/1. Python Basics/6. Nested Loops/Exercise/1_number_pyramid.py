number = int(input())
flag = True
counter = 0

for i in range(1, number + 1):
    for j in range(1, i + 1):
        counter += 1
        print(f"{counter} ", end="")
        if counter == number:
            flag = False
            break
    if not flag:
        break
    print()
