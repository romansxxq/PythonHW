import json
users = {}

def AddUser():
    userName = input("Enter your name: ")
    userPassword = input("Enter your password: ")

    users[userName] = userPassword

def ChangePassword():
    userName = input("Enter your name: ")
    if userName in users:
        changePassword = input("Enter your new password: ")
        if changePassword == users[userName]:
            print("Error")
        else:
            users[userName] = changePassword
    else:
        print("Error")


def RemoveUser():
    userName = input("Enter your name: ")
    if userName in users:
        users.pop(userName)
    else:
        print("This user wasn`t found :(")

def CheckPassword():
    userName = input("Enter your name: ")
    if userName in users:
        if len(users[userName]) < 6:
            print("Your password is too short")
        else:
            print("Good :)")

def SaveUser():
    try:
        with open("users.json", "w") as file:
            json.dump(users, file)
        print("Users saved successfully")
    except Exception as e:
        print(f"Error saving users: {e}")

def LoadUser():
    global users
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
        print("Users loaded successfully")
    except Exception as e:
        print(f"Error loading users: {e}")
        users = {}

def ViewUser():
    if users:
        print("Users:")
        for username, password in users.items():
            print(f"{username}: {password}")
    else:
        print("No users found")

def main():
    LoadUser()
    while True:
        print("1. Add user")
        print("2. View user")
        print("3. Change password")
        print("4. Remove user")
        print("5. Check password")
        print("6. Save abd leave")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            AddUser()
        elif choice == 2:
            ViewUser()
        elif choice == 3:
            ChangePassword()
        elif choice == 4:
            RemoveUser()
        elif choice == 5:
            CheckPassword()
        elif choice == 6:
            SaveUser()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()