# Data Input
n = int(input())
L = int(input())

# Logic and Print Output
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(ord("a"), ord("a") + L):
            for m in range(ord("a"), ord("a") + L):
                for n in range(1, n + 1):
                    if n > i and n > j:
                        print(f"{i}{j}{chr(k)}{chr(m)}{n}", end=" ")
