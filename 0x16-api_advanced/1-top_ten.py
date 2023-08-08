#!/usr/bin/python3
"""Defines function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
        """Get the title of the first 10 host posts on a given subreddit."""
            url = "https://www.reddit.com/r/{}.json?limit=10".format(subreddit)
                head = {'User-Agent': 'Surumen Notebook'}
                    res = requests.get(url, headers=head).json()
                        if not res.get('data', {}).get('children', []):
                                    print('None')
                                        else:
                                                    for val in res['data']['children']:
                                                                    print(val['data']['title'])
