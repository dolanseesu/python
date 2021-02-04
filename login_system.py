# a small login system

userlist = {"Peter": {"pw": "1234"}, "Hans": {"pw": "987"}}

def add_user(username):
    if username not in userlist:
        pw = str(input("Please enter a password: "))
        userlist.update({username:{"pw": pw}})
        return True
    else:
        print("This user already exists, please choose another one")
        return False

def login():
    username = str(input("Please enter your username: "))
    if username not in userlist:
        print("Username not found.")
        if input("Would you like to create a new one? (y/n): ") != "y":
            return
        else:
            if add_user(str(input("Please enter a username: "))) == True:
                print("User successfully added.")
            return 
    pw = str(input("Please enter your password: "))
    if userlist[username]["pw"] != pw:
        print("Incorrect Password")
        return
    print("Welcome {}".format(username))

login()