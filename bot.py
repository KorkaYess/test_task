import os
import json
import random
import requests


URL = 'http://0.0.0.0:8000/api/'
headers = {
    'headers': 'application/json',
    'Content-Type': 'application/json'
}


def create_users(user_number):
    credentials = []
    register_url = URL + 'register'
    headers = {
        'headers': 'application/json',
        'Content-Type': 'application/json'
    }

    for user in range(user_number):
        username = f"test_{user}"
        payload = {
            "username": username,
            "password":"test_pass",
            "first_name":"Firstname",
            "last_name":"Lastname"
        }
        response = requests.request("POST", register_url, headers=headers, json=payload)
        if response.status_code == 200:
            response = json.loads(response.text)
            credentials.append({
                "user": response["user"]["id"],
                "creds": {
                    "username": username,
                    "password":"test_pass",
                }
            })

    print(f'Succesfully signed up {len(credentials)} users of {user_number}.')
    return credentials


def sign_in(credentials):
    tokens = []
    token_url = URL + 'token/'
    headers = {
        'headers': 'application/json',
        'Content-Type': 'application/json'
    }

    for payload in credentials:
        response = requests.request("POST", token_url, headers=headers, json=payload['creds'])
        if response.status_code == 200:
            response = json.loads(response.text)
            tokens.append({
                "user_id": payload["user"],
                "username": payload["creds"]["username"],
                "access": response["access"],
            })

    print(f'Succesfully signed in {len(tokens)} users {len(credentials)}.')
    return tokens


def create_posts(tokens, post_count):
    posts = []
    post_url = URL + 'create-post'

    for user in tokens:
        for post in range(random.randint(1, post_count)):
            payload = {
                "title": f"Post{post}-by-{user['username']}",
                "description": "description of post",
            }
            headers = {
                'Authorization': f'Bearer {user["access"]}',
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", post_url, headers=headers, json=payload)

            if response.status_code == 201:
                response = json.loads(response.text)
                posts.append(response["id"])

    print(f'Succesfully created {len(posts)} posts.')
    return posts


def create_likes(tokens, posts, likes_count):
    likes = []
    like_url = URL + 'create-like'

    for user in tokens:
        for like in range(random.randint(1, likes_count)):
            payload = {
                "value": random.randint(0, 1),
                "post": random.choice(posts),
            }
            headers = {
                'Authorization': f'Bearer {user["access"]}',
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", like_url, headers=headers, json=payload)

            if response.status_code == 201:
                response = json.loads(response.text)
                likes.append(response["id"])

    print(f'Succesfully created {len(likes)} likes.')
    return posts


def start():
    with open('config.json') as json_file:
        data = json.load(json_file)

        credentials = create_users(data['number_of_users'])
        tokens = sign_in(credentials)
        posts = create_posts(tokens, data['max_posts_per_user'])
        likes = create_likes(tokens, posts, data['max_likes_per_user'])


if __name__ == "__main__":
    start()
