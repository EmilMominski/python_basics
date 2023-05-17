# Read User Input
type_cinema = input()  # Premiere, Normal, Discount
rows = int(input())
columns = int(input())
price = 0

# Logic
seats = rows * columns
if type_cinema == "Premiere":
    price = 12
elif type_cinema == "Normal":
    price = 7.5
elif type_cinema == "Discount":
    price = 5
income = price * seats

# Print Output
print(f"{income:.2f} leva.")
