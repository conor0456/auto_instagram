import requests
import json
from decouple import config

def generate_token():
    response = requests.get("https://graph.facebook.com/v15.0/oauth/access_token",
        params={
            "grant_type": "fb_exchange_token",
            "client_id": config('INSTAGRAM_CLIENT_ID'),
            "client_secret": config('INSTAGRAM_CLIENT_SECRET'),
            "fb_exchange_token": config('INSTAGRAM_GENERATED_TOKEN')
        })
    json_data = json.loads(response.text)
    print(json_data['access_token'])
    return json_data['access_token']

def generate_post():
    url = f"https://graph.facebook.com/v15.0/{config('INSTAGRAM_USER_ID')}/media"
    print(url)
    payload = {
        'image_url': 'https://media.nga.gov/iiif/a8c923e1-078d-4f94-b1f4-0e303afe2155__640/full/!740,560/0/default.jpg',
        'caption': 'A real Rothko',
        'access_token': config('INSTAGRAM_GENERATED_TOKEN')
    }
    r = requests.post(url, data=payload)
    print(r.text)

generate_post()
