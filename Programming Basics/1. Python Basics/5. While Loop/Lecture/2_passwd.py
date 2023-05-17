username = input()
password = input()
passwd_guess = input()
while passwd_guess != password:
    passwd_guess = input()
print(f"Welcome {username}!")
