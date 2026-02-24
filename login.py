# login.py

def login():
    users_file = "users.txt"
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    try:
        with open(users_file, "r") as f:
            users = [line.strip().split(",") for line in f.readlines()]
    except FileNotFoundError:
        print("No users found. Please signup first.")
        return

    for user in users:
        if user[0] == username and user[2] == password:
            print("Login successful!")
            return
    
    print("Invalid username or password.")

if __name__ == "__main__":
    login()