import tweepy

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)

# Replace with the username of the targeted profile
target_username = 'targeted_profile_username'

# Get the ID of the targeted profile
user = api.get_user(screen_name=target_username)
target_profile_id = user.id_str

# Get the latest tweet from the targeted profile
latest_tweet = api.user_timeline(user_id=target_profile_id, count=1)[0]

# Post a comment as a reply to the latest tweet
comment_text = 'This is my comment.'
api.update_status(comment_text, in_reply_to_status_id=latest_tweet.id_str)






#Write: 3,000 Tweets per month-$100.00 USD/month
