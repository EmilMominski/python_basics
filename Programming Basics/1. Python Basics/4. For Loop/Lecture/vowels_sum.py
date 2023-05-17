random_text = input()
vowels_sum = 0

for i in random_text:
    if i == "a":
        vowels_sum = vowels_sum + 1
    if i == "e":
        vowels_sum = vowels_sum + 2
    if i == "i":
        vowels_sum = vowels_sum + 3
    if i == "o":
        vowels_sum = vowels_sum + 4
    if i == "u":
        vowels_sum = vowels_sum + 5

print(vowels_sum)
