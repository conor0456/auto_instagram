from pyfacebook import GraphAPI
from decouple import config
import requests
import json

INSTAGRAM_BUSINESS_ID = config('INSTAGRAM_USER_ID')
api = GraphAPI(access_token=config('INSTAGRAM_GENERATED_TOKEN'))

def post_file_to_instagram_with_caption(url, caption):
    print(f"Publishing photo stored at {url}")
    try:
        data = api.post_object(
            object_id=INSTAGRAM_BUSINESS_ID,
            connection="media",
            params={
                "image_url": url,
                "caption": caption,
            },
        )
        container_id = data["id"]
        print(f"Published photo to container, receieved id: {container_id}")
        publish_data = api.post_object(
            object_id=INSTAGRAM_BUSINESS_ID,
            connection="media_publish",
            params={
                "creation_id": container_id,
            },
        )
        print("Image published!")
    except:
        print(f"Failed to publish photo to Instagram")

# This method is used to convert a short lived token to a long lived token
def exchange_short_token_for_long_token(short_lived_user_access_token):
    response = requests.get("https://graph.facebook.com/v15.0/oauth/access_token",
        params={
            "grant_type": "fb_exchange_token",
            "client_id": config('INSTAGRAM_CLIENT_ID'),
            "client_secret": config('INSTAGRAM_CLIENT_SECRET'),
            "fb_exchange_token": short_lived_user_access_token
        })
    json_data = json.loads(response.text)
    print(json_data)
    print(json_data['access_token'])
