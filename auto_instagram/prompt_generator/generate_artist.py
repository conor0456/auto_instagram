import os
import random

def fetch_random_artist():
    dir = os.path.dirname(__file__)
    lines = open(os.path.join(dir, "artists.csv")).read().splitlines()
    return random.choice(lines).title()
