import praw
import os

# reddit app secret and personal use script stored in environment variables
id=os.getenv('client_id')
secret=os.getenv('secret')
user=os.getenv('r_username')
passcode=os.getenv('r_password')


# from reddit app 
reddit = praw.Reedit(userAgent=True, client_id=id,
                     client_secret=secret, username=user, password=passcode)


