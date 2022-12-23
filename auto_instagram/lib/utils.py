from decouple import config
import os
from argparse import ArgumentParser

dir = os.path.dirname(__file__)
parser = ArgumentParser()
parser.add_argument("-p", "--post_to_instagram")
parser.add_argument("-u", "--upscale_image")
parser.add_argument("-l", "--store_locally")
parser.add_argument("-r", "--store_remotely")
parser.add_argument("-s", "--subject_override")
arguments = parser.parse_args()

def print_run_configs():
    print(f"""
Running script with configs:
Post To Instagram: {should_post_to_instagram()}
Upscale Image: {should_upscale_image()}
Persist Image Locally: {should_persist_image_locally()}
Persist image Remotely: {should_persist_image_remotely()}
Subject Override: {subject_override()}
    """)

def should_post_to_instagram():
    return coalesce_config_with_arguments(read_argument_bool_value('post_to_instagram'), read_optional_bool_config('POST_TO_INSTAGRAM')) or False

def should_upscale_image():
    return coalesce_config_with_arguments(read_argument_bool_value('upscale_image'), read_optional_bool_config('UPSCALE_IMAGE')) or False

def should_persist_image_locally():
    return coalesce_config_with_arguments(read_argument_bool_value('store_locally'), read_optional_bool_config('PERSIST_IMAGES_LOCALLY')) or False

def should_persist_image_remotely():
    return coalesce_config_with_arguments(read_argument_bool_value('store_remotely'), read_optional_bool_config('PERSIST_IMAGES_REMOTELY')) or False

def subject_override():
    subject_override = coalesce_config_with_arguments(arguments.subject_override, read_optional_string_config('SUBJECT_OVERRIDE'))
    if subject_override is not None:
        return subject_override.title()
    return None

def coalesce_config_with_arguments(argument_value, config_value):
    # Prefer passed in arguments over config
    if argument_value is None:
        return config_value
    else:
        return argument_value

def read_mandatory_bool_config(config_name):
    return config(config_name, cast=bool)

def read_optional_bool_config(config_name):
    try:
        return config(config_name, cast=bool)
    except Exception as e:
        print(f"Failed to read optional config {config_name}, defaulting to None")
        return None

def read_mandatory_string_config(config_name):
    return config(config_name, cast=string).strip()

def read_optional_string_config(config_name):
    try:
        return config(config_name, cast=str).strip()
    except Exception as e:
        print(f"Failed to read optional config {config_name}, defaulting to None")
        return None

def read_argument_bool_value(argument_name):
    if getattr(arguments, argument_name) is not None:
        return getattr(arguments, argument_name).strip().lower() == 'true'
    return None

def clean_up_local_image(file_name):
    print(f"Deleting local file: {file_name}")
    path = os.path.join(dir, '..','..','images', file_name)
    os.remove(path)
