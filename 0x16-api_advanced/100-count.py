#!/usr/bin/python3
"""Defines a function that queries the Reddit API."""
import requests
from collections import defaultdict


def count_words(subreddit, word_list, dfdict=defaultdict(int), after=None):
        """parses the titles of all hot articels, and prints a sorted count\
                    of given keywords (case-insensitive).
                        """
                            if not word_list:
                                        return

                                        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
                                            header = {'User-Agent': 'Lekerios Notebook'}

                                                res = requests.get(url, headers=header, allow_redirects=False)
                                                    if res.status_code != 200:
                                                                return None

                                                                if after is not None:
                                                                            url += '?after={}'.format(after)
                                                                                else:
                                                                                            word_list = [word.lower() for word in word_list]

                                                                                                for val in res.json()['data'].get('children', []):
                                                                                                            title = val['data']['title'].lower().split()
                                                                                                                    for word in title:
                                                                                                                                    if word in word_list:
                                                                                                                                                        dfdict[word] += 1

                                                                                                                                                            after = res.json()['data'].get('after')
                                                                                                                                                                if not after:
                                                                                                                                                                            if dfdict:
                                                                                                                                                                                            tmp = ["{}: {:d}".format(key, dfdict[key])
                                                                                                                                                                                                                       for key in sorted(dfdict, key=dfdict.get, reverse=True)]
                                                                                                                                                                                                        print("\n".join(tmp))
                                                                                                                                                                                                            else:
                                                                                                                                                                                                                        return count_words(subreddit, word_list, dfdict, after)
