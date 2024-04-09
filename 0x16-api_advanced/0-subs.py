#!/usr/bin/python3
"""Quering Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Quering a subreddit and retrieving number
    of subscribers.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'My user Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data= response.json().get('dat'{})
        subCount = data.get('subscribers', 0)
        return subCount
    else:
        return 0
