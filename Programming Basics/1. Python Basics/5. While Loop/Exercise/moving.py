# Read User's Input
width = int(input())
length = int(input())
height = int(input())
boxes = input()
current_boxes = 0

# Logic
max_boxes = width * length * height
while current_boxes < max_boxes and boxes != "Done":
    boxes_digit = int(boxes)
    current_boxes += boxes_digit
    if current_boxes >= max_boxes:
        continue
    boxes = input()
difference = current_boxes - max_boxes
abs_difference = abs(difference)

# Print Output
if difference < 0:
    print(f"{abs_difference} Cubic meters left.")
else:
    print(f"No more free space! You need {abs_difference} Cubic meters more.")
