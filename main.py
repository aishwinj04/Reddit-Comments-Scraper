import praw
import os

# reddit app secret and personal use script stored in environment variables
id=os.getenv('client_id')
secret=os.getenv('secret')
user=os.getenv('r_username')
passcode=os.getenv('r_password')


# from reddit app 
reddit = praw.Reddit(user_agent='My Reddit Bot', client_id=id, client_secret=secret, username=user, password=passcode)


url = 'https://www.reddit.com/r/vscode/comments/1htzfkm/try_it_these_6_vscode_settings_will_bring_your/'

post = reddit.submission(url)
print(post)
