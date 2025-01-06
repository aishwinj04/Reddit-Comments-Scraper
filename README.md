# Reddit Comment Scraper

This Python program allows you to scrape the top comments from any Reddit post and export them into a CSV file for further analysis. It uses the [PRAW](https://praw.readthedocs.io/en/latest/) library to interact with Reddit and the [Pandas](https://pandas.pydata.org/) library for data manipulation.

## Features

- Scrape top-level comments from a Reddit post.
- Save the data to a CSV file for analysis.
- Simple user interface for copying and pasting Reddit post URLs.

## Requirements

- Python 3.7+
- Libraries: `praw`, `pandas`
- Reddit account credentials (stored securely in environment variables)

# Set your Reddit API credentials as environment variables:

- `client_id` - Your Reddit API client ID.
- `client_secret` - Your Reddit API client secret.
- `r_username` - Your Reddit username.
- `r_password` - Your Reddit password.

### Example on Linux or macOS:

```
export client_id='your_client_id'
export secret='your_client_secret'
export r_username='your_reddit_username'
export r_password='your_reddit_password'
```

#### Sample post links to test:
- https://www.reddit.com/r/books/comments/13ka9ky/what_is_a_book_you_think_everyone_needs_to_read/
- https://www.reddit.com/r/ExperiencedDevs/comments/oket8j/whats_your_favorite_interview_question/
- https://www.reddit.com/r/AskReddit/comments/id46ym/what_simple_life_hack_should_everyone_know/
