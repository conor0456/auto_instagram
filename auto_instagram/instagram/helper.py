from decouple import config

HASHTAGS = ['#ai', '#aiart', '#aiartwork', '#aiartists', '#aiartcommunity', '#aiartdaily', '#aiartist']


def build_caption(title, image_generation_prompt, summary):
    hashtags = " ".join(HASHTAGS)
    return f"{title} \n\nImage generated with the prompt: {image_generation_prompt} \n\n{summary} \n\n{hashtags}"
