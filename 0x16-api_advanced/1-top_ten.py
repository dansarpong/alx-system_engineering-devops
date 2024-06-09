#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "u/DannyCypher_"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        [print(k.get("data").get("title")) for k in results.get("children")]
    else:
        print("None")
