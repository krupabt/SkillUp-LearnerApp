# api_integration.py
import requests

def fetch_data():
    # Example API call to a placeholder JSON API
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Fetched Data:")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
        return data
    else:
        print("Failed to fetch data")
        return None

if __name__ == "__main__":
    fetch_data()