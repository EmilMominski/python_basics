# Data Input
required_height = int(input())

# Logic & Print Output
height = required_height - 30
jump_count = 0
while height <= required_height:
    current_jump = 0
    unsuccessful_jumps = 0
    for i in range(3):
        jump = int(input())
        jump_count += 1
        if jump > height:
            current_jump += jump
            break
        else:
            unsuccessful_jumps += 1
    if current_jump > height:
        if height == required_height:
            print(f"Tihomir succeeded, he jumped over {height}cm after {jump_count} jumps.")
            break
        else:
            height += 5
            continue
    if unsuccessful_jumps == 3:
        print(f"Tihomir failed at {height}cm after {jump_count} jumps.")
        break
