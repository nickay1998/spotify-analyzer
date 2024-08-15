import requests

def get_token():
    from .auth import get_token
    return get_token()

def get_data(url):
    headers = {"Authorization": "Bearer " + get_token()}
    response = requests.get(url, headers = headers)

    if response.status_code != 200:
        print(f"Error occurred. Status code: {response.status_code}")
    
    return response.json()

def post_data(url, headers, data):
    response = requests.post(url, headers = headers, data = data)

    if response.status_code != 200:
        print(f"Error occurred. Status code: {response.status_code}")
    
    return response.json()