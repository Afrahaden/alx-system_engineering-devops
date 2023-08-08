#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers for a
given subreddit."""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Get the number of subscribers on a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = requests.utils.default_headers()
    headers = {'User-Agent': 'Surumens Notebook'}
    header.update(headers)
    res = requests.get(url, headers=header).json()

    count = res.get('data', {}).get('subscribers')
    if not count:
        return 0
    return count


if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))
