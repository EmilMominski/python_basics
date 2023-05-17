# Read User's Input
searched_book = input()
book = input()
book_counter = 0
flag = True

# Logic
while book != "No More Books":
    if book == searched_book:
        flag = False
        break
    else:
        book_counter += 1
        book = input()

# Print Output
if not flag:
    print(f"You checked {book_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")
