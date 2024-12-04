import requests

# Your Facebook Graph API access token
access_token = ''  # Replace with your actual token

# Define the URL to fetch user data (including friends' birthdays)
url = f'https://graph.facebook.com/me/friends?fields=name,birthday&access_token={access_token}'

def get_friends_birthday(url):
    try:
        print("deepak-1")
        response = requests.get(url)
        data = response.json()

        # Check if there is a 'data' key
        if 'data' in data:
            print("deepak-2")
            print("data:", data)
            for friend in data['data']:
                print("deepak-3")
                name = friend.get('name', 'N/A')
                print("name:", name)
                birthday = friend.get('birthday', 'N/A')
                print(f"{name}: {birthday}")
        else:
            print("No friends data found or invalid access token.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Fetch and display the birthday data
get_friends_birthday(url)
