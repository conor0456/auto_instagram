from decouple import config
import os

dir = os.path.dirname(__file__)

def print_run_configs():
    print(f"""
Running script with configs:
Post To Instagram: {should_post_to_instagram()}
Upscale Image: {should_upscale_image()}
Persist Image Locally: {should_persist_image_locally()}
Persist image Remotely: {should_persist_image_remotely()}
    """)

def should_post_to_instagram():
    return read_bool_config('POST_TO_INSTAGRAM')

def should_upscale_image():
    return read_bool_config('UPSCALE_IMAGE')

def should_persist_image_locally():
    return read_bool_config('PERSIST_IMAGES_LOCALLY')

def should_persist_image_remotely():
    return read_bool_config('PERSIST_IMAGES_REMOTELY')

def read_bool_config(config_name):
    value = config(config_name)
    if value is None:
        return False
    else:
        return value.strip().lower() == 'true'

def clean_up_local_image(file_name):
    print(f"Deleting local file: {file_name}")
    path = os.path.join(dir, '..','..','images', file_name)
    os.remove(path)
