#!/usr/bin/python3
"""Fetch posts from JSONPlaceholder and process them."""
import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print the status code and titles."""
    response = requests.get(URL)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save id, title, body into posts.csv."""
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()
        data = []
        for post in posts:
            data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
