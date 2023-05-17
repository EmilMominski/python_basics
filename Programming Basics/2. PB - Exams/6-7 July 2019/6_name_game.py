# Read User's Input
import sys
name = input()

# Logic
score = 0
name_score = 0
winner = ""
max_score = -sys.maxsize

while name != "Stop":
    name_length = len(name)
    score = 0
    for i in range(name_length):
        digit = int(input())
        if digit == ord(name[i]):
            score += 10
        else:
            score += 2
    name_score = score
    if name_score >= max_score:
        winner = name
        max_score = name_score
    name = input()

# Print Output
print(f"The winner is {winner} with {max_score} points!")
