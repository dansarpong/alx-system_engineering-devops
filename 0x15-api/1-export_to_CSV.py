#!/usr/bin/python3
"""Returns to-do list information for a given employee ID"""
import csv
import requests
import sys

if __name__ == "__main__":
    u_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/" + u_id).json()
    username = user.get("username")
    todos = requests.get(url + "/users/" + u_id + "/todos").json()

    with open("{}.csv".format(u_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [u_id, username, task.get("completed"), task.get("title")]
        ) for task in todos]
