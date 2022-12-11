from decouple import config

def build_caption(title, image_generation_prompt, summary):
    return f"{title} \n\n Image generated with the prompt: {image_generation_prompt} \n\n {summary}"
