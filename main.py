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


def to_csv(table, filename):
    table.to_csv(f'csv_outputs/{filename}.csv', index=False)


def main():
    link = input('Copy & Paste the link to the Reddit Post below:\n')
    post = get_post(link)
    data = get_comments(post)

    filename = input('Processing Complete....\nEnter filename (without extension) to save to: ')

    to_csv(data, filename)

    print('Done!')
    print(f'Total comments: {len(post.comments)}')


if __name__ == '__main__':
    main()
