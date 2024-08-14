import requests
import sys
import csv
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from environment variables
api_key = os.getenv("RAPIDAPI_KEY")

if not api_key:
    print("API key not found in .env file.")
    sys.exit(1)

def insta_following(username):
    print(f"Fetching 10000 following.... this may take a while")

    url = "https://instagram-scraper-api2.p.rapidapi.com/v1/following"
    querystring = {"username_or_id_or_url": username, "amount": "1000"}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "instagram-scraper-api2.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Check for HTTP errors
        fetchedRes = response.json()

        count = fetchedRes['data']['count']
        items = fetchedRes['data']['items']

        print(f"Count: {count}")

        os.makedirs('./csv_result', exist_ok=True)

        with open(f'./csv_result/{username}_following.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Full Name', 'Username', 'User ID', 'Private', 'Verified', 'Profile Picture']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for item in items:
                full_name = item.get('full_name', 'N/A')
                user_id = item['id']
                is_private = item['is_private']
                is_verified = item['is_verified']
                profile_pic_url = item['profile_pic_url']
                username = item['username']
                
                print(f"Name: {full_name}, Username: {username}")
                print(f"Private: {is_private}")
                print(f"Verified: {is_verified}")
                print(f"Profile Picture: {profile_pic_url}")
                print("-" * 30)
                
                writer.writerow({
                    'Full Name': full_name,
                    'Username': username,
                    'User ID': user_id,
                    'Private': is_private,
                    'Verified': is_verified,
                    'Profile Picture': profile_pic_url
                })
        print(f"")
        print(f"Fetched {count} following")
        print(f"Data has been exported in 'csv_result' folder.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    insta_following(username)
