# Read User's Input
not_satisfactory_marks = int(input())
problem_title = input()
problem_mark = int(input())
not_satisfactory_counter = 1
problem_counter = 1
mark_sum = 0
last_problem_title = ""
flag = True

# Logic
while problem_title != "Enough":
    if problem_mark <= 4:
        if not_satisfactory_counter >= not_satisfactory_marks:
            flag = False
            break
        else:
            not_satisfactory_counter += 1
    mark_sum += problem_mark
    last_problem_title = problem_title
    problem_title = input()
    if problem_title == "Enough":
        continue
    problem_mark = int(input())
    problem_counter += 1
average_mark = mark_sum / problem_counter

# Print Output
if flag:
    print(f"Average score: {average_mark:.2f}")
    print(f"Number of problems: {problem_counter}")
    print(f"Last problem: {last_problem_title}")
else:
    print(f"You need a break, {not_satisfactory_marks} poor grades.")
