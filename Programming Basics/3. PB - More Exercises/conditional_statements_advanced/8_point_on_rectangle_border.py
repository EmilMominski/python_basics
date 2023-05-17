# Data Input
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

# Logic
flag = False
if x1 <= x <= x2:
    if y == y1 or y == y2:
        flag = True
if y1 <= y <= y2:
    if x == x1 or x == x2:
        flag = True

# Print Output
if flag:
    print("Border")
else:
    print("Inside / Outside")
