number = int(input())
sum_numbers = 0

while True:
    if sum_numbers >= number:
        print(sum_numbers)
        break
    data = int(input())
    sum_numbers = sum_numbers + data
