# Data Input
import sys
number_of_films = int(input())

# Logic
sum_of_ratings = 0
highest_film_rating = -sys.maxsize
lowest_film_rating = sys.maxsize
for i in range(number_of_films):
    film_title = input()
    film_rating = float(input())
    if film_rating > highest_film_rating:
        highest_film_rating = film_rating
        film_with_highest_rating = film_title
    if film_rating < lowest_film_rating:
        lowest_film_rating = film_rating
        film_with_lowest_rating = film_title
    sum_of_ratings += film_rating
average_rating = sum_of_ratings / number_of_films

# Print Output
print(f"{film_with_highest_rating} is with highest rating: {highest_film_rating:.1f}")
print(f"{film_with_lowest_rating} is with lowest rating: {lowest_film_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
