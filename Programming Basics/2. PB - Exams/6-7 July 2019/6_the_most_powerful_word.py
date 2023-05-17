# Read User's input
import sys
import math

word = input()

# Logic
max_word_sum = -sys.maxsize
word_sum = 0
most_powerful_word = ""

while word != "End of words":
    word_length = len(word)
    word_sum = 0
    flag = True
    for i in range(word_length):
        if i == 0:
            if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" \
                    or word[i] == "u" or word[i] == "y" or word[i] == "A" \
                    or word[i] == "E" or word[i] == "I" or word[i] == "O" \
                    or word[i] == "U" or word[i] == "Y":
                flag = False
        word_sum += ord(word[i])
    if not flag:
        word_sum = word_sum * word_length
    else:
        word_sum = math.floor(word_sum / word_length)
    if word_sum > max_word_sum:
        most_powerful_word = word
        max_word_sum = word_sum
    word = input()

# Print Output
print(f"The most powerful word is {most_powerful_word} - {max_word_sum}")
