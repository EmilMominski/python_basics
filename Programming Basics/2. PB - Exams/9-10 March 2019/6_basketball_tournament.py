# Data Input
name_of_tournament = input()

# Logic
total_games = 0
total_wins = 0
total_losses = 0
while name_of_tournament != "End of tournaments":
    games = int(input())
    number_games = 0
    wins = 0
    losses = 0
    for i in range(games):
        number_games += 1
        team_points = int(input())
        enemy_points = int(input())
        difference = abs(team_points - enemy_points)
        if team_points > enemy_points:
            wins += 1
            print(f"Game {number_games} of tournament {name_of_tournament}: win with "
                f"{difference} points.")
        else:
            losses += 1
            print(f"Game {number_games} of tournament {name_of_tournament}: lost with "
                f"{difference} points.")
    total_wins += wins
    total_losses += losses
    total_games += games
    name_of_tournament = input()
games_won = total_wins * 100 / total_games
games_lost = total_losses * 100 / total_games

# Print Output
print(f"{games_won:.2f}% matches win")
print(f"{games_lost:.2f}% matches lost")
