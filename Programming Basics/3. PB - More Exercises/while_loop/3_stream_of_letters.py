# Data Input
letter = input()

# Logic and Print Output
output_string = str()
c_counter = 0
o_counter = 0
n_counter = 0
while letter != "End":
    if letter == "A" or letter == "B" or letter == "C" or letter == "D" or letter == "E" or letter == "F" \
        or letter == "G" or letter == "H" or letter == "I" or letter == "J" or letter == "K" or letter == "L" \
        or letter == "M" or letter == "N" or letter == "O" or letter == "P" or letter == "Q" or letter == "R" \
        or letter == "S" or letter == "T" or letter == "U" or letter == "V" or letter == "W" or letter == "X" \
        or letter == "Y" or letter == "Z" or letter == "a" or letter == "b" or letter == "c" or letter == "d" \
        or letter == "e" or letter == "f" or letter == "g" or letter == "h" or letter == "i" or letter == "j" \
        or letter == "k" or letter == "L" or letter == "m" or letter == "n" or letter == "o" or letter == "p" \
        or letter == "q" or letter == "r" or letter == "s" or letter == "t" or letter == "u" or letter == "v" \
            or letter == "w" or letter == "x" or letter == "y" or letter == "z":
        if letter != "c" and letter != "o" and letter != "n":
            output_string = output_string + letter
        elif letter == "c":
            c_counter += 1
            if c_counter > 1:
                output_string = output_string + letter
        elif letter == "o":
            o_counter += 1
            if o_counter > 1:
                output_string = output_string + letter
        elif letter == "n":
            n_counter += 1
            if n_counter > 1:
                output_string = output_string + letter
    if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
        print(output_string, end=" ")
        c_counter = 0
        o_counter = 0
        n_counter = 0
        output_string = str()
    letter = input()
