number = int(input())

stars = 1
if number % 2 == 0:
    stars += 1
left_right = (number - 1) // 2

# upper part of the diamond
for i in range((number + 1) // 2):
    print("-" * left_right, end="")
    print("*", end="")
    mid = number - 2 * left_right - 2
    if mid >= 0:
        print("-" * mid, end="")
        print("*", end="")
    print("-" * left_right)
    left_right -= 1

# lower part of the diamond
left_right = 0
for i in range((number - 1) // 2):
    left_right += 1
    print("-" * left_right, end="")
    print("*", end="")
    mid = number - 2 * left_right - 2
    if mid >= 0:
        print("-" * mid, end="")
        print("*", end="")
    print("-" * left_right)
