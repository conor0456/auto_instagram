import csv
import os
from pathlib import Path

columns = ['subject', 'title', 'summary', 'file_name']
dir = os.path.dirname(__file__)
file_path = os.path.join(dir, '..','..', 'generated_results.csv')


def save_entry(subject, title, summary, file_name):
    if os.path.isfile(file_path):
        print('Found storage file, appending row')
        with open(file_path, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([subject, title, summary, file_name])
    else:
        print('No storage file found, creating new one')
        with open(file_path, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(columns)
            csvwriter.writerow([subject, title, summary, file_name])
