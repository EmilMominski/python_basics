# Read User's Input
import sys
movie = input()

# Logic
movie_counter = 0
max_result = -sys.maxsize
movie_winner = ""
while movie != "STOP":
    movie_counter += 1
    if movie_counter == 7:
        print("The limit is reached.")
        break
    movie_digit = len(movie)
    sum_counter = 0
    for i in range(movie_digit):
        sum_counter += ord(movie[i])
    for j in range(movie_digit):
        if movie[j].islower():
            sum_counter -= movie_digit * 2
        elif movie[j].isupper():
            sum_counter -= movie_digit
    if sum_counter > max_result:
        max_result = sum_counter
        movie_winner = movie
    movie = input()

# Print Output
print(f"The best movie for you is {movie_winner} with {max_result} ASCII sum.")
