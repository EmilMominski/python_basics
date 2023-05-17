name = input()
student_class = int(input())
amount_of_marks = 1
expelled_counter = 0
sum_of_all_marks = 0
average_mark = 0
flag = True

while amount_of_marks <= 12:
    mark = float(input())
    if mark < 4:
        expelled_counter += 1
        if expelled_counter > 1:
            print(f"{name} has been excluded at {student_class} grade")
            flag = False
            break
    else:
        sum_of_all_marks += mark
        amount_of_marks += 1
        average_mark = sum_of_all_marks / 12
if flag:
    print(f"{name} graduated. Average grade: {average_mark:.2f}")
