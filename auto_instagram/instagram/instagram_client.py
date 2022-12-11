from pyfacebook import GraphAPI
from decouple import config

ACCESS_TOKEN =
INSTAGRAM_BUSINESS_ID = config('INSTAGRAM_USER_ID')

api = GraphAPI(access_token=config('INSTAGRAM_GENERATED_TOKEN'))

data = api.post_object(
    object_id=INSTAGRAM_BUSINESS_ID,
    connection="media",
    params={
        "image_url": "https://media.nga.gov/iiif/a8c923e1-078d-4f94-b1f4-0e303afe2155__640/full/!740,560/0/default.jpg",
        "caption": "Image by api",
    },
)
print(data)
# {'id': '17952987976782688'}
# Get your container id.
container_id = data["id"]

# Then publish the container.
publish_data = api.post_object(
    object_id=INSTAGRAM_BUSINESS_ID,
    connection="media_publish",
    params={
        "creation_id": container_id,
    },
)
print(publish_data)
