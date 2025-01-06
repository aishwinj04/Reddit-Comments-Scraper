import praw
import os
import pandas as df 

# reddit app secret and personal use script stored in environment variables
id=os.getenv('client_id')
secret=os.getenv('secret')
user=os.getenv('r_username')
passcode=os.getenv('r_password')


# initialize reddit instanece and get post 
def get_post(post_link):

    reddit = praw.Reddit(user_agent='My Reddit Bot', client_id=id, client_secret=secret, username=user, password=passcode)

    post = reddit.submission(url=post_link)

    return post



