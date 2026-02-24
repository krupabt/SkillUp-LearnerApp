# notifications.py

def send_notification(user, message):
    print(f"Sending notification to {user}: {message}")

def list_notifications(user):
    notifications = [
        "Welcome to the app!",
        "Your settings have been updated.",
        "You have a new message."
    ]
    print(f"Notifications for {user}:")
    for n in notifications:
        print("-", n)

if __name__ == "__main__":
    user = "user123"
    send_notification(user, "This is a test notification.")
    list_notifications(user)