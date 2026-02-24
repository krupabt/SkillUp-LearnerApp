# signup.py

def signup():
    users_file = "users.txt"
    
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    # Read existing users
    try:
        with open(users_file, "r") as f:
            users = [line.strip().split(",")[0] for line in f.readlines()]
    except FileNotFoundError:
        users = []

    if username in users:
        print("User already exists!")
    else:
        with open(users_file, "a") as f:
            f.write(f"{username},{email},{password}\n")
        print("Signup successful!")

if __name__ == "__main__":
    signup()