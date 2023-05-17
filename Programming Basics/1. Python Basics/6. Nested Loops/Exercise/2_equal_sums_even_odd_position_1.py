number_1 = int(input())
number_2 = int(input())

for i in range(number_1, number_2 + 1):
    even_sum = 0
    odd_sum = 0
    number_to_string = str(i)
    for j in range(len(number_to_string)):
        if j % 2 == 0:
            even_sum += int(number_to_string[j])
        elif j % 2 != 0:
            odd_sum += int(number_to_string[j])
    if even_sum == odd_sum:
        print(f"{i} ", end="")
