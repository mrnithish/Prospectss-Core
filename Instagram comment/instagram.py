from instagram_private_api import Client, ClientCompatPatch

# Replace with your own Instagram credentials
username = 'sooniyakarannaveen@gmail.com'
password = 'Naveen@123'

# Replace with the target Instagram username
target_username = 'nithish_blank' #id

# Initialize the Instagram API client
api = Client(username, password)
api.login()
try:
    # Get the target user's ID
    target_user = api.username_info(target_username)
    target_user_id = target_user['user']['pk']

    # Get the user's feed
    user_feed = api.user_feed(target_user_id)

    # Get the latest post
    latest_post = user_feed['items'][0]

    # Post a comment on the latest post
    comment_text = 'Super broo' #comment
    api.post_comment(latest_post['id'], comment_text)

    # Logout from the Instagram API client
    api.logout()
    print("successful")
except:
    print("Private Account")
