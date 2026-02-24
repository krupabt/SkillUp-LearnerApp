# local_storage.py
import json
import os

STORAGE_FILE = "local_storage.json"

def save_data(key, value):
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[key] = value
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f)
    print(f"Data saved: {key} -> {value}")

def read_data(key):
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            data = json.load(f)
        return data.get(key, "No data found")
    return "No data found"

if __name__ == "__main__":
    save_data("user123", "Sample Item")
    print("Reading from local storage:", read_data("user123"))