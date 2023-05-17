import sys
easter_bread = int(input())

max_score = -sys.maxsize
max_score_baker = ""
for i in range(easter_bread):
    score = 0
    baker = input()
    while True:
        value = input()
        if value == "Stop":
            print(f"{baker} has {score} points.")
            break
        else:
            digit = int(value)
            score += digit
    if score > max_score:
        max_score = score
        max_score_baker = baker
        print(f"{baker} is the new number 1!")

print(f"{max_score_baker} won competition with {max_score} points!")
