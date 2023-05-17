import math
first_competitor = int(input())
second_competitor = int(input())
third_competitor = int(input())

sum_in_seconds = first_competitor + second_competitor + third_competitor
minutes = sum_in_seconds // 60
minutes = math.floor(minutes)
seconds = sum_in_seconds % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
