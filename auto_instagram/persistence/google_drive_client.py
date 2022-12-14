from __future__ import print_function

import google.auth
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from decouple import config
import requests

SCOPES = ['https://www.googleapis.com/auth/drive']
AUTHORIZATION_URL = "https://oauth2.googleapis.com/token"
FOLDER_ID = config('GOOGLE_DRIVE_IMAGE_DIRECTORY_ID')
dir = os.path.dirname(__file__)

def upload_file_to_drive(file_name):
    try:
        access_token = generate_token()
        creds = google.oauth2.credentials.Credentials(access_token)
        service = build('drive', 'v3', credentials=creds)
        file_metadata = {
            'name': file_name,
            'parents': [FOLDER_ID]
        }
        media = MediaFileUpload(os.path.join(dir, '..','..','images', file_name),
                                mimetype='image/jpg')
        print(f"Uploading file {file_name} to google drive")
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()
        print("successfully uploaded file to google drive")
    except Exception as e:
        print(f"Encountered error: {e} when attempting to save to google drive, skipping for now")

def generate_token():
    params = {
            "grant_type": "refresh_token",
            "client_id": config('GOOGLE_DRIVE_CLIENT_ID'),
            "client_secret": config('GOOGLE_DRIVE_CLIENT_SECRET'),
            "refresh_token": config('GOOGLE_DRIVE_CLIENT_REFRESH_TOKEN')
    }

    r = requests.post(AUTHORIZATION_URL, data=params)
    if r.ok:
        print("Generated auth token for google drive")
        return r.json()['access_token']
    else:
        return None
