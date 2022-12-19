import os
import random

def fetch_random_subject():
    dir = os.path.dirname(__file__)
    lines = open(os.path.join(dir, "subjects.csv")).read().splitlines()
    return random.choice(lines).title()
