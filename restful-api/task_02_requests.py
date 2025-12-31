#!/usr/bin/python3

"""
This module fetches posts from JSONPlaceholder API,
prints them, and saves them to a CSV file.
"""

import requests
import csv


url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch posts from API and print status code + titles
    """
    res = requests.get(url)
    print("Status Code:", res.status_code)

    if res.status_code == 200:
        posts = res.json()
        for post in posts:
            print(post["title"])
    else:
        print("Request failed")


def fetch_and_save_posts():
    """
    Fetch posts from API and save them into posts.csv
    """
    res = requests.get(url)

    if res.status_code == 200:
        posts = res.json()

        info = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(info)

    else:
        print("Request failed")
