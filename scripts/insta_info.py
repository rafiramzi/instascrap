import requests
import sys
import csv
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("RAPIDAPI_KEY")

if not api_key:
    print("API key not found in .env file.")
    sys.exit(1)


def insta_info(username):
    print(f"Fetching info for {username}...")

    url = "https://instagram-scraper-api2.p.rapidapi.com/v1/info"
    querystring = {"username_or_id_or_url": username}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "instagram-scraper-api2.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        fetchedRes = response.json()

        data = fetchedRes['data']

        username = data['username']
        full_name = data['full_name']
        about = data.get('about', {})
        country = about.get('country', 'N/A') if about else 'N/A'
        bio_email = data.get('biography_email', 'N/A')
        follower = data['follower_count']
        following = data['following_count']
        user_id = data['id']
        phone_number = data.get('contact_phone_number', 'N/A')
        public_number = data['public_phone_number']
        biography = data['biography']
        profile_pic_url = data['profile_pic_url_hd']

        print("-" * 30)
        print(f"Username: {username}")
        print(f"Full Name: {full_name}")
        print(f"Country: {country}")
        print(f"ID: {user_id}")
        print(f"Following : {following}")
        print(f"Follower : {follower}")
        print(f"Public Phone Number: {public_number}")
        print(f"Phone Number: {phone_number}")
        print(f"Bio Email : {bio_email}")
        print(f"Bio Content : {biography}")
        print(f"Profile Picture: {profile_pic_url}")
        print("-" * 30)

        os.makedirs('./csv_result', exist_ok=True)
        csv_filename = f"./csv_result/{username}_info.csv"
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "Username", "Full Name", "Country", "User ID", 
                "Following", "Follower", "Public Phone Number", 
                "Phone Number", "Bio Email", "Bio Content", 
                "Profile Picture URL"
            ])
            writer.writerow([
                username, full_name, country, user_id, 
                following, follower, public_number, 
                phone_number, bio_email, biography, profile_pic_url
            ])

        print(f"Data has been exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
