username = "MICHAEL"
password = 2345

user1 = str(input("Please enter Username: ").upper())

try:
    if user1 == username:
        print(f"Welcome {username}")
    else:
        print("Wrong username")
        exit("Try again")

    user2 = int(input("Please enter Password: "))

    if user2 == password:
        print("Password correct, yeepee!")


except ValueError:
    print("Wrong password, try again")

