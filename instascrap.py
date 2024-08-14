from scripts.insta_follower import insta_follower
from scripts.insta_following import insta_following
from scripts.new_api import update_env


def show_banner():
    with open('scripts/banner.txt', 'r') as file:
        banner = file.read()
    print(banner)

def menu():
    print("Choose an option:")
    print("[1] Fetch Instagram Followers")
    print("[2] Fetch Instagram Following")
    print("[3] Exit")
    print("")
    print("Configuration:")
    print("[4] Set your API key")
    print("")
    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter the Instagram username: ")
        insta_follower(username)
    elif choice == '2':
        username = input("Enter the Instagram username: ")
        insta_following(username)
    elif choice == '3':
        print("Exiting the program...")
        exit()
    elif choice == '4':
        new_api = input("Your API key: ")
        update = update_env(new_api)
        if update:
            print("API key updated successfully")
    else:
        print("Invalid choice, please try again.")
        menu()

show_banner()
menu()
