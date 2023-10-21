import requests

def shorten_url(long_url):
    base_url = "https://api-ssl.bitly.com/v4/shorten"

    access_token = "YOUR_ACCESS_TOKEN"  # Replace with your Bitly access token

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    data = {
        "long_url": long_url
    }

    response = requests.post(base_url, headers=headers, json=data)
    if response.status_code == 200:
        short_url = response.json()["link"]
        return short_url
    else:
        print("Failed to shorten URL.")
        error_message = response.json()["message"]
        print("Error message:", error_message)
        return None

# Get the long URL from user input
url = input("Enter the long URL: ")

# Use the shorten_url function to shorten the URL
shortened_url = shorten_url(url)
if shortened_url:
    print("Short URL:", shortened_url)
