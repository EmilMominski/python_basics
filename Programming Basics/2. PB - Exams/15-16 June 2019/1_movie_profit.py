movie_title = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
cinema_commission = int(input())

ticket_profit = tickets * ticket_price * days
profit = ticket_profit - ticket_profit * cinema_commission / 100
print(f"The profit from the movie {movie_title} is {profit:.2f} lv.")
