number = int(input())
matches = 0
for i in range(number + 1):
    for j in range(number + 1):
        for k in range(number + 1):
            result = i + j + k
            if result == number:
                matches += 1
print(matches)
