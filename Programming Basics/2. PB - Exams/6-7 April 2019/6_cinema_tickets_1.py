# Data Input
film_title = input()
available_seats = int(input())

# Logic
total_ticket_amount = 0
total_student_tickets = 0
total_standard_tickets = 0
total_kid_tickets = 0

while film_title != "Finish":
    student_tickets = 0
    standard_tickets = 0
    kid_tickets = 0
    for i in range(available_seats):
        ticket_purchased = input()    # student, standard, kid
        if ticket_purchased == "End":
            break
        else:
            if ticket_purchased == "student":
                student_tickets += 1
            elif ticket_purchased == "standard":
                standard_tickets += 1
            elif ticket_purchased == "kid":
                kid_tickets += 1
    tickets_purchased_per_film = student_tickets + standard_tickets + kid_tickets
    percent_seats_taken = tickets_purchased_per_film * 100 / available_seats
    total_ticket_amount += tickets_purchased_per_film
    total_student_tickets += student_tickets
    total_standard_tickets += standard_tickets
    total_kid_tickets += kid_tickets
    print(f"{film_title} - {percent_seats_taken:.2f}% full.")
    film_title = input()
    if film_title == "Finish":
        continue
    else:
        available_seats = int(input())
percent_student = total_student_tickets * 100 / total_ticket_amount
percent_standard = total_standard_tickets * 100 / total_ticket_amount
percent_kid = total_kid_tickets * 100 / total_ticket_amount

# Print Output
print(f"Total tickets: {total_ticket_amount}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")