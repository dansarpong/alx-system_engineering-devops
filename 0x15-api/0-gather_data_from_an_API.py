#!/usr/bin/python3
"""Returns to-do list information for a given employee ID"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/" + sys.argv[1]).json()
    todos = requests.get(url + "/users/" + sys.argv[1] + "/todos").json()
    done = [fin.get("title") for fin in todos if fin.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)
    ))
    [print("\t {}".format(task)) for task in done]
