import os
import sys
from dotenv import load_dotenv, set_key

def update_env(api_key):
    if api_key:
        dotenv_path = '.env'
        load_dotenv(dotenv_path)
        set_key(dotenv_path, 'RAPIDAPI_KEY', api_key)
        return True
    else:
        print("No token provided.")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No API key provided")
        sys.exit(1)

    api_key = sys.argv[1]
    update_env(api_key)
    print("API key updated successfully")
