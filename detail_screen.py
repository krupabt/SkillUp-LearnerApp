# detail_screen.py

def detail_screen(item_name, item_description):
    print("Detail Screen")
    print("[Navigation Icon] <- Back")
    print(f"Item: {item_name}")
    print(f"Description: {item_description}")

if __name__ == "__main__":
    detail_screen("Sample Item", "This is a detailed description of the sample item.")