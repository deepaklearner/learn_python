 To fetch easily the bday, create a python based web scrapper to scrap birthday from my facebook friends.

 To create a Python-based web scraper to extract birthday information from your Facebook friends, you would typically need to:

1. **Access Facebook Data:** First, you must access your Facebook profile and friends list, as well as the birthday information. Unfortunately, scraping Facebook directly via unofficial means violates their terms of service. However, there is a legitimate way to get this information using the **Facebook Graph API** (which is legal and safe, as long as you follow Facebook’s developer guidelines).

2. **Use Facebook Graph API:**
   - The Facebook Graph API allows you to access certain data from your account, including birthdays of your friends (if privacy settings permit).
   - You would need to create a Facebook Developer Account, set up an app, and obtain a User Access Token to interact with the API.

Here's an outline of how you can fetch birthdays using the **Facebook Graph API** and Python:

### Steps to Use Facebook Graph API for Birthday Data:

#### 1. Set up Facebook Developer Account & Create App:
- Go to the [Facebook Developer Portal](https://developers.facebook.com/).
- Create an app and obtain an **App ID** and **App Secret**.
- Generate a **User Access Token** (this will require permission from Facebook to access your data). You can get the token through the [Facebook Access Token Tool](https://developers.facebook.com/tools/explorer/).

#### 2. Install the Necessary Python Libraries:
```bash
pip install requests
```

#### 3. Create the Python Script:

Here’s a basic script to fetch birthday data from Facebook using the Graph API.

```python
import requests

# Your Facebook Graph API access token
access_token = 'your_access_token_here'  # Replace with your actual token

# Define the URL to fetch user data (including friends' birthdays)
url = f'https://graph.facebook.com/me/friends?fields=name,birthday&access_token={access_token}'

def get_friends_birthday(url):
    try:
        response = requests.get(url)
        data = response.json()

        # Check if there is a 'data' key
        if 'data' in data:
            for friend in data['data']:
                name = friend.get('name', 'N/A')
                birthday = friend.get('birthday', 'N/A')
                print(f"{name}: {birthday}")
        else:
            print("No friends data found or invalid access token.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Fetch and display the birthday data
get_friends_birthday(url)
```

### Explanation:
1. **Access Token:** Replace `'your_access_token_here'` with the token you generated in the Facebook Developer tools. This token gives you access to your data, including friends' birthdays.
2. **Graph API Request:** The URL `https://graph.facebook.com/me/friends` fetches a list of your friends. You can specify additional fields such as `name` and `birthday` to get the desired data.
3. **Handling Responses:** The script checks the JSON response to see if it contains the necessary data and then prints out the name and birthday of each friend.

### 4. Run the Script:
Once you have the script set up with a valid access token, run it to fetch your Facebook friends' birthdays.

### Important Notes:
- **Privacy Settings:** If a friend has restricted their birthday visibility, you will not be able to retrieve that data.
- **API Limits:** Facebook imposes API rate limits, so be careful when making multiple requests in a short period of time.
- **Permissions:** Ensure that your app has the proper permissions to access friends' birthday information. You might need to request specific permissions like `user_friends` and `friends_birthday` via the OAuth flow.

By following these steps, you can legally fetch birthdays using the Graph API without violating Facebook’s terms of service.



https://www.facebook.com/v13.0/dialog/oauth?
  client_id=640357040011525
  &redirect_uri=http://localhost:8000/callback
  &scope=user_friends,friends_birthday
  &response_type=EAAJGZAr3mOQUBOZBsR91aJkHe1sHrf4BOTfGeng9046f6TlmvkgmBNzyBn6cOnlrZBgav3sf6YZCgZBNHTByf0rrxVB7XsYAlmNNcGpBveCdNY3ZBFskEurGEYPL3hRCWDyaXXTu9Yd0T7nBYyFN92HCRHflqOA9w5c6sZCUPJZBbAZBuFueXy6e1FnMZBGkpa9JrnN1RLtZCP9Vsz1cCG7Sap3mZBYscNVxfsPSuuJfGWxn0Mf6GDKvyuVtMnOsxJWNaHsZD
