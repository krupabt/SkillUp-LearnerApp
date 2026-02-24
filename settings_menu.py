# settings_menu.py

def settings_menu():
    settings = {
        "Notifications": True,
        "Dark Mode": False,
        "Language": "English"
    }

    print("Settings Menu:")
    for key, value in settings.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    settings_menu()