n = int(input())
special_counter = 0

for i in range(1111, 10000):
    number_to_string = str(i)
    number_to_string_length = len(number_to_string)
    for j in range(number_to_string_length):
        digit = int(number_to_string[j])
        if digit == 0:
            continue
        if n % digit == 0:
            special_counter += 1
        else:
            special_counter = 0
    if special_counter == int(number_to_string_length):
        print(f"{i} ", end="")
    special_counter = 0
