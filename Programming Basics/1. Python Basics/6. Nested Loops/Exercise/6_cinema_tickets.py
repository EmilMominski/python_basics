# Read User's Input
film_title = input()
available_seats = int(input())
ticket_counter = 0
total_ticket_counter = 0
student_ticket_counter = 0
standard_ticket_counter = 0
kid_ticket_counter = 0

# Logic
while film_title != "Finish":
    ticket_type = input()       # student, standard or kid
    while ticket_type != "End":
        ticket_counter += 1
        if ticket_type == "student":
            student_ticket_counter += 1
        elif ticket_type == "standard":
            standard_ticket_counter += 1
        elif ticket_type == "kid":
            kid_ticket_counter += 1
        if ticket_counter >= available_seats:
            break
        ticket_type = input()
    percent_seats = ticket_counter * 100 / available_seats
    print(f"{film_title} - {percent_seats:.2f}% full.")
    total_ticket_counter += ticket_counter
    ticket_counter = 0
    film_title = input()
    if film_title == "Finish":
        continue
    available_seats = int(input())

total_student_percent = student_ticket_counter * 100 / total_ticket_counter
total_standard_percent = standard_ticket_counter * 100 / total_ticket_counter
total_kid_percent = kid_ticket_counter * 100 / total_ticket_counter

# Print Output
print(f"Total tickets: {total_ticket_counter}")
print(f"{total_student_percent:.2f}% student tickets.")
print(f"{total_standard_percent:.2f}% standard tickets.")
print(f"{total_kid_percent:.2f}% kids tickets.")
