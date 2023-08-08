#!/usr/bin/python3
"""Defines a function that queries the Reddit API."""
import requests


def recurse(subreddit, hot_list=[], after=None):
        """returns a list of titles of all host articles for a given subreddit.
            """
                url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
                    if after is not None:
                                url += "?after={}".format(after)

                                    head = {'User-Agent': "Surumens Notebook"}

                                        res = requests.get(url, headers=head, allow_redirects=False)
                                            if res.status_code != 200:
                                                        return None

                                                        for val in res.json()['data'].get('children', []):
                                                                    hot_list.append(val['data']['title'])

                                                                        if res.json()['data'].get('after'):
                                                                                    return recurse(subreddit, hot_list,
                                                                                                                   after=res.json()['data'].get('after'))
                                                                                        return hot_list
