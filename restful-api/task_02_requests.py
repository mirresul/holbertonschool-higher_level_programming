#!/usr/bin/python3
"""Task 02 - Consuming API data using Python requests"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save them into a CSV file"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        formatted_data = []

        for post in data:
            formatted_data.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(formatted_data)
