import os, sys
import openai
from decouple import config
from datetime import date
import urllib.request
openai.api_key = config('OPEN_AI_TOKEN')


def generate_file_name(image_url, image_generation_prompt, subject):
    today = date.today()
    day = today.strftime("%Y_%m_%d")
    prompt_hash = str(abs(hash(image_generation_prompt)))[:5]
    clean_subject = "_".join(subject.strip().lower().split(" "))
    dir = os.path.dirname(__file__)
    return os.path.join(dir, '..','..','images', f"{day}_{clean_subject}_{prompt_hash}.jpg")

def generate_and_save_image(image_generation_prompt, subject):
    print(f"Generating image for prompt: {image_generation_prompt}")
    response = openai.Image.create(
      prompt=image_generation_prompt,
      n=1,
      size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(f"Generated image at url: {image_url}")

    file_name = generate_file_name(image_url, image_generation_prompt, subject)
    urllib.request.urlretrieve(image_url, file_name)
    print(f"Finished downloading file locally to: {file_name}")

def generate_image_generation_prompt(subject):
    prompt = interpolate_subject(config('IMAGE_PROMPT_GENERATION_PROMPT'), subject)
    print(f"Building image generation prompt with prompt: {prompt}")
    completion = fetch_completion(prompt)
    result = completion.choices[0].text.strip()
    print(f"Built image generation prompt: {result}")
    return result

def generate_subject_summary(subject):
    prompt = interpolate_subject(config('SUMMARY_GENERATION_PROMPT'), subject)
    print(f"Building subject summary with prompt: {prompt}")
    completion = fetch_completion(prompt)
    result = completion.choices[0].text.strip()
    print(f"Built subject summary: {result}")
    return result

def interpolate_subject(string, subject):
    return string.replace('{subject}', subject)

def fetch_completion(prompt):
    return openai.Completion.create(engine=config('GENERATIVE_TEXT_ENGINE'),
    prompt=prompt,
    max_tokens=2048)
