from decouple import config
import random
import os

def generate_prompt():
    artist = config('ARTIST_STYLE')
    art_style = config('ART_STYLE')
    noun = fetch_random_noun_from_csv()
    #prompt = f"a {art_style} of a {noun} in the style of {artist}"
    prompt = "Create a portrait of Frida Kahlo using a machine learning algorithm"
    print(f"Generated prompt: {prompt}")
    return prompt

# def generate_random_word():
    # all_words = [word for synset in wn.all_synsets('n') for word in synset.lemma_names()]
    # filtered_array = [x for x in all_words if len(x)>=3]
    # noun = random.choice(filtered_array)

def fetch_random_noun_from_csv():
    dir = os.path.dirname(__file__)
    lines = open(os.path.join(dir, "nouns.csv")).read().splitlines()
    return random.choice(lines)
