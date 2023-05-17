# Read User's Input
student_name = input()
class_counter = 1
sum_of_marks = 0
excluded_counter = 1
flag = True

# Logic
while class_counter <= 12:
    mark_text = input()
    mark_digit = float(mark_text)
    if mark_digit < 4:
        if excluded_counter > 1:
            flag = False
            break
        excluded_counter += 1
    else:
        sum_of_marks += mark_digit
        class_counter += 1

# Print Output
if flag:
    average_grade = sum_of_marks / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{student_name} has been excluded at {class_counter} grade")
