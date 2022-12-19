from decouple import config
import os
from argparse import ArgumentParser

dir = os.path.dirname(__file__)
parser = ArgumentParser()
parser.add_argument("-p", "--post_to_instagram")
parser.add_argument("-u", "--upscale_image")
parser.add_argument("-l", "--store_locally")
parser.add_argument("-r", "--store_remotely")
arguments = parser.parse_args()

def print_run_configs():
    print(f"""
Running script with configs:
Post To Instagram: {should_post_to_instagram()}
Upscale Image: {should_upscale_image()}
Persist Image Locally: {should_persist_image_locally()}
Persist image Remotely: {should_persist_image_remotely()}
    """)

def should_post_to_instagram():
    return coalesce_config_with_arguments(arguments.post_to_instagram, 'POST_TO_INSTAGRAM')

def should_upscale_image():
    return coalesce_config_with_arguments(arguments.upscale_image, 'UPSCALE_IMAGE')

def should_persist_image_locally():
    return coalesce_config_with_arguments(arguments.store_locally, 'PERSIST_IMAGES_LOCALLY')

def should_persist_image_remotely():
    return coalesce_config_with_arguments(arguments.store_remotely, 'PERSIST_IMAGES_REMOTELY')

def coalesce_config_with_arguments(argument_value, config_name):
    # Prefer passed in arguments over config
    if argument_value is None:
        return read_bool_config(config_name)
    else:
        return argument_value.strip().lower() == 'true'

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
