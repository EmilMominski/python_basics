# Data Input
last_sector = input()
rows_count_first = int(input())
seats_odd_row = int(input())

# Logic & Print Output
current_rows_count = rows_count_first
counter = 0
for sector in range(ord("A"), ord(last_sector) + 1):
    for rows in range(1, current_rows_count + 1):
        if rows % 2 != 0:
            seats_count = seats_odd_row
        else:
            seats_count = seats_odd_row + 2
        for seats in range(ord("a"), ord("a") + seats_count):
            counter += 1
            print(f"{chr(sector)}{rows}{chr(seats)}")
    current_rows_count += 1
print(counter)
