password = input("Password:" )
while True:
    again_password = input("Repeat password: ")
    if password == again_password:
        print("User account created!")
        break  
    elif password != again_password:
        print("They do not match!")    