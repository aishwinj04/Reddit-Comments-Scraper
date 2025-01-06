import praw
import os
import pandas as df 

# reddit app secret and personal use script stored in environment variables
id=os.getenv('client_id')
secret=os.getenv('secret')
user=os.getenv('r_username')
passcode=os.getenv('r_password')


# from reddit app 
reddit = praw.Reddit(user_agent='My Reddit Bot', client_id=id, client_secret=secret, username=user, password=passcode)


url = 'https://www.reddit.com/r/TorontoMetU/comments/18jxacd/anyone_know_some_of_the_easiest_table_a_lower/'

post = reddit.submission(url=url)
title = post.title
body = post.selftext

print(post.title)

# get all comments
post.comments.replace_more(limit=None)

data = []

print(len(post.comments))
for comment in post.comments.list():
    data.append({
        'User': comment.author,
        'Comment': comment.body,
        'Score': comment.score 
    })


to_df = df.DataFrame(data)
print(to_df)
    
# now add to a csv file 
to_df.to_csv('results.csv', index=False)


