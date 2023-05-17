# Data Input
length = float(input())
width = float(input())

# Logic
rows_in_length = length // 1.2
rows_in_width = (width - 1) // 0.7
number_work_places = rows_in_length * rows_in_width - 3

# Print Output
print(number_work_places)