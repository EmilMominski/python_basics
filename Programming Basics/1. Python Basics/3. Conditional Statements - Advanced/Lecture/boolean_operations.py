a = 50
b = 200
c = 300

if (a >= 100 and b <= 200) or (c + b >= 300 and c <= 400):
    print("Yes")

if a >= 100 and (b <= 200 or c + b >= 300) and c <= 400:
    print("Yes")
    