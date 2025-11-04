#!/usr/bin/python3
"""
Basic Python script to fetch posts from JSONPlaceholder using requests.get()
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder, prints the status code,
    and then prints the titles of all posts if the request was successful.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()

            print("\nTitles of Posts:")
            for post in posts:
                print(f"- {post['title']}")
        else:
            print(f"Request failed with status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching posts for printing: {e}")


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder, structures the data,
    and saves it to a CSV file named 'posts.csv'.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()

        posts_data = response.json()

        if posts_data:
            
            fieldnames = ['id', 'title', 'body']

            with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for post in posts_data:
                    
                    writer.writerow({k: post.get(k, '') for k in fieldnames})
            print("\nSuccessfully fetched posts and saved them to 'posts.csv'")
        else:
            print("No posts found to save.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching posts for saving: {e}")
    except IOError as e:
        print(f"An error occurred while writing to the CSV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("Fetching and Printing Posts")
    fetch_and_print_posts()

    print("\nFetching and Saving Posts to CSV")
    fetch_and_save_posts()
