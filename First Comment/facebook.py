import facebook

# Replace with your own Facebook access token
access_token = 'your_access_token'

# Replace with the target Facebook profile ID or username
target_profile_id = 'target_profile_id_or_username'

# Initialize the Graph API object
graph = facebook.GraphAPI(access_token)

# Create the comment on the targeted profile
comment_text = 'helloooo guys'

# Post the comment on the targeted profile
graph.put_object(target_profile_id, 'comments', message=comment_text)



