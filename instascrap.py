from scripts.insta_follower import insta_follower
from scripts.insta_following import insta_following
from scripts.insta_info import insta_info
from scripts.new_api import update_env


def show_banner():
    with open('scripts/banner.txt', 'r') as file:
        banner = file.read()
    print(banner)

def menu():
    print("Choose an option:")
    print("[1] Fetch User Info")
    print("[2] Fetch User Followers")
    print("[3] Fetch User Following")
    print("[4] Exit")
    print("")
    print("Configuration:")
    print("[5] Set your API key")
    print("")
    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter the Instagram username: ")
        insta_info(username)

    elif choice == '2':
        username = input("Enter the Instagram username: ")
        insta_follower(username)
    elif choice == '3':
        username = input("Enter the Instagram username: ")
        insta_following(username)
    elif choice == '4':
        print("Exiting the program...")
        exit()
    elif choice == '5':
        new_api = input("Your API key: ")
        update = update_env(new_api)
        if update:
            print("API key updated successfully")
    else:
        print("Invalid choice, please try again.")
        menu()

show_banner()
menu()
