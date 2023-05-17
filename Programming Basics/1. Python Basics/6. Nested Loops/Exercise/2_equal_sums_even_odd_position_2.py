first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num + 1):
    even_sum = 0
    odd_sum = 0
    number_to_string = str(number)
    for index, digit in enumerate(number_to_string):
        if index % 2 == 0:
            even_sum += int(digit)
        elif index % 2 != 0:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end=" ")
