# settings_screen.py

def settings_screen():
    print("Settings Screen")
    settings = {
        "Notifications": True,
        "Dark Mode": False,
        "Language": "English",
        "Privacy": "Standard"
    }
    for key, value in settings.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    settings_screen()