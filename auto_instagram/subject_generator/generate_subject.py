import os
import random
import csv
from decouple import config

dir = os.path.dirname(__file__)

def fetch_random_subject():
    lookback_window = fetch_lookback_window()
    list_of_subjects = fetch_subjects()
    previous_subjects = fetch_previous_subjects()
    if lookback_window == 0 or len(previous_subjects) == 0:
        return random.choice(list_of_subjects)
    for previous_subject in previous_subjects:
        if previous_subject in list_of_subjects:
            list_of_subjects.remove(previous_subject)
    if len(list_of_subjects) == 0:
        raise Exception('No subjects available after removing the subjects from the lookback threshold')
    return random.choice(list_of_subjects)

def fetch_previous_subjects():
    lookback_window = fetch_lookback_window()
    previous_subjects = []
    with open(os.path.join(dir, '..', '..', "generated_results.csv"), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        if csv_reader is None:
            return []
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count +=1
            else:
                previous_subjects.append(row['subject'])
                line_count += 1
    if len(previous_subjects) >= lookback_window:
        previous_subjects = previous_subjects[-lookback_window:]
    return previous_subjects

def fetch_subjects():
    subjects = []
    with open(os.path.join(dir, "subjects.csv"), mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            subjects.append(row[0].title())
    if len(subjects) == 0:
        raise Exception('Could not find any subjects in the subjects file')
    return subjects

def fetch_lookback_window():
    value = config('RESAMPLING_LOOKBACK_THRESHOLD')
    if value is None:
        return 0
    return int(value)
