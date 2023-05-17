# Data Input
movie_title = input()
""" A Star Is Born, Bohemian Rhapsody, Green Book, The Favourite"""
hall_type = input()    # normal, luxury, ultra luxury
ticket_sold = int(input())

# Logic
if movie_title == "A Star Is Born":
    if hall_type == "normal":
        income = ticket_sold * 7.5
    elif hall_type == "luxury":
        income = ticket_sold * 10.5
    elif hall_type == "ultra luxury":
        income = ticket_sold * 13.5
elif movie_title == "Bohemian Rhapsody":
    if hall_type == "normal":
        income = ticket_sold * 7.35
    elif hall_type == "luxury":
        income = ticket_sold * 9.45
    elif hall_type == "ultra luxury":
        income = ticket_sold * 12.75
elif movie_title == "Green Book":
    if hall_type == "normal":
        income = ticket_sold * 8.15
    elif hall_type == "luxury":
        income = ticket_sold * 10.25
    elif hall_type == "ultra luxury":
        income = ticket_sold * 13.25
elif movie_title == "The Favourite":
    if hall_type == "normal":
        income = ticket_sold * 8.75
    elif hall_type == "luxury":
        income = ticket_sold * 11.55
    elif hall_type == "ultra luxury":
        income = ticket_sold * 13.95

# Output
print(f"{movie_title} -> {income:.2f} lv.")
