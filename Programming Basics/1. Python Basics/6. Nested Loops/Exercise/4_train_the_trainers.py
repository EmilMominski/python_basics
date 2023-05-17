jury_number = int(input())
presentation_title = input()
presentation_mark_sum = 0
presentation_counter = 0
average_sum_marks = 0

while presentation_title != "Finish":
    presentation_counter += 1

    for i in range(1, jury_number + 1):
        mark = float(input())
        presentation_mark_sum += mark

    average_presentation_mark = presentation_mark_sum / jury_number
    average_sum_marks += average_presentation_mark
    print(f"{presentation_title} - {average_presentation_mark:.2f}.")
    presentation_mark_sum = 0
    presentation_title = input()

total_average_mark = average_sum_marks / presentation_counter
print(f"Student's final assessment is {total_average_mark:.2f}.")
