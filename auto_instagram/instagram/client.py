from pyfacebook import GraphAPI
from decouple import config

INSTAGRAM_BUSINESS_ID = config('INSTAGRAM_USER_ID')
api = GraphAPI(access_token=config('INSTAGRAM_GENERATED_TOKEN'))

def post_file_to_instagram_with_caption(url, caption):
    print(f"Publishing photo stored at {url}")
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
