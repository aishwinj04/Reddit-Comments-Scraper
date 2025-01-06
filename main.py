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


# get top comments given the reddit post
def get_comments(post):

    post.comments.replace_more(limit=0)  # only top level comments
    data = []

    # add into dictionary for df
    for comment in post.comments:
        data.append({
            'User': comment.author,
            'Comment': comment.body,
            'Score': comment.score
        })

    table = df.DataFrame(data)
    return table

# create the output file


