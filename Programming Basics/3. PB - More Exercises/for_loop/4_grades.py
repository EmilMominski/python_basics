# Data Input
students_count = int(input())

# Logic
mark_2 = 0
mark_3 = 0
mark_4 = 0
mark_5 = 0
total_marks = 0
for i in range(1, students_count + 1):
    mark = float(input())
    if 2 <= mark <= 2.99:
        mark_2 += 1
    elif 3 <= mark <= 3.99:
        mark_3 += 1
    elif 4 <= mark <= 4.99:
        mark_4 += 1
    elif mark >= 5:
        mark_5 += 1
    total_marks += mark
mark_2_percent = mark_2 * 100 / students_count
mark_3_percent = mark_3 * 100 / students_count
mark_4_percent = mark_4 * 100 / students_count
mark_5_percent = mark_5 * 100 / students_count
average_mark = total_marks / students_count

# Print Output
print(f"Top students: {mark_5_percent:.2f}%")
print(f"Between 4.00 and 4.99: {mark_4_percent:.2f}%")
print(f"Between 3.00 and 3.99: {mark_3_percent:.2f}%")
print(f"Fail: {mark_2_percent:.2f}%")
print(f"Average: {average_mark:.2f}")
