import os, sys
import openai
from decouple import config
from datetime import date
import urllib.request
openai.api_key = config('OPEN_AI_TOKEN')


def generate_file_name(image_generation_prompt, subject):
    today = date.today()
    day = today.strftime("%Y_%m_%d")
    prompt_hash = str(abs(hash(image_generation_prompt)))[:5]
    clean_subject = "_".join(subject.strip().lower().split(" "))
    return f"{day}_{clean_subject}_{prompt_hash}.jpg"

def build_file_path(file_name):
    dir = os.path.dirname(__file__)
    return os.path.join(dir, '..','..','images', file_name)

def generate_and_save_image(image_generation_prompt, subject):
    print(f"Generating image for prompt: {image_generation_prompt}")
    response = openai.Image.create(
      prompt=image_generation_prompt,
      n=1,
      size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(f"Generated image at url: {image_url}")

    file_name = generate_file_name(image_generation_prompt, subject)
    urllib.request.urlretrieve(image_url, build_file_path(file_name))
    print(f"Finished downloading file locally to: {file_name}")
    return image_url

def generate_image_generation_prompt(subject):
    prompt = interpolate_subject(config('IMAGE_PROMPT_GENERATION_PROMPT'), subject)
    print(f"Building image generation prompt with prompt: {prompt}")
    result = fetch_completion(prompt)
    print(f"Built image generation prompt: {result}")
    return result

def generate_subject_summary(subject):
    prompt = interpolate_subject(config('SUMMARY_GENERATION_PROMPT'), subject)
    print(f"Building subject summary with prompt: {prompt}")
    result = fetch_completion(prompt)
    print(f"Built subject summary: {result}")
    return result

def generate_image_title(image_generation_prompt):
    prompt = interpolate_image_generation_prompt(config('TITLE_GENERATION_PROMPT'), image_generation_prompt)
    print(f"Building title with prompt: {prompt}")
    result = fetch_completion(prompt)
    print(f"Built title: {result}")
    return result

def interpolate_subject(string, subject):
    return string.replace('{SUBJECT}', subject)

def interpolate_image_generation_prompt(string, image_generation_prompt):
    return string.replace('{IMAGE_GENERATION_PROMPT}', f"'{image_generation_prompt}'")

def fetch_completion(prompt):
    completion = openai.Completion.create(engine=config('GENERATIVE_TEXT_ENGINE'), prompt=prompt, max_tokens=2048)
    return completion.choices[0].text.strip()

