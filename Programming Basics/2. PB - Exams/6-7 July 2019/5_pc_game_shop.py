# Read User's Input
games_sold = int(input())

# Logic
hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0

for _ in range(games_sold):
    game_title = input()
    if game_title == "Hearthstone":
        hearthstone_counter += 1
    elif game_title == "Fornite":
        fornite_counter += 1
    elif game_title == "Overwatch":
        overwatch_counter += 1
    else:
        others_counter += 1
percent_hearthstone = hearthstone_counter * 100 / games_sold
percent_fornite = fornite_counter * 100 / games_sold
percent_overwatch = overwatch_counter * 100 / games_sold
percent_others = others_counter * 100 / games_sold

# Print Output
print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")
