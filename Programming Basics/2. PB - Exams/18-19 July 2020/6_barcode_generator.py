beginning_of_range = int(input())
end_of_range = int(input())

beginning_word = str(beginning_of_range)
end_word = str(end_of_range)

beginning_i = int(beginning_word[0])
end_i = int(end_word[0])

beginning_j = int(beginning_word[1])
end_j = int(end_word[1])

beginning_k = int(beginning_word[2])
end_k = int(end_word[2])

beginning_m = int(beginning_word[3])
end_m = int(end_word[3])

for i in range(beginning_i, end_i + 1):
    for j in range(beginning_j, end_j + 1):
        for k in range(beginning_k, end_k + 1):
            for m in range(beginning_m, end_m + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and m % 2 != 0:
                    print(f"{i}{j}{k}{m} ", end="")
