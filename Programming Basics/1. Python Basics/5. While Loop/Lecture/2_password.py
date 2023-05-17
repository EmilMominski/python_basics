username = input()
user_password = input()

while True:
    password = input()
    if user_password == password:
        break
print(f"Welcome: {username}!")
