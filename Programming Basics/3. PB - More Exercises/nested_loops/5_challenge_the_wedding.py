# Data Input
men = int(input())
women = int(input())
tables = int(input())

# Logic & Print Output
table_counter = 0
for man_client in range(1, men + 1):
    for woman_client in range(1, women + 1):
        print(f"({man_client} <-> {woman_client}) ", end="")
        table_counter += 1
        if table_counter == tables:
            break
    if table_counter == tables:
        break
