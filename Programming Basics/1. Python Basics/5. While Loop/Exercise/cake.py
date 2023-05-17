# Read User's Input
length = int(input())
width = int(input())
command = input()
pieces = 0

# Logic
max_pieces = length * width
while pieces < max_pieces and command != "STOP":
    command_digit = int(command)
    pieces += command_digit
    if pieces >= max_pieces:
        continue
    command = input()
difference = pieces - max_pieces
abs_difference = abs(difference)

# Print Output
if difference < 0:
    print(f"{abs_difference} pieces are left.")
else:
    print(f"No more cake left! You need {abs_difference} pieces more.")
