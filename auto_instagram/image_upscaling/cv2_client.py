import cv2
import os
from decouple import config

dir = os.path.dirname(__file__)
model_path = os.path.join(dir, "models/LapSRN_x8.pb")

def upscale_and_overwrite_image(file_name):
    image_path = os.path.join(dir, '..','..','images', file_name)
    print(f"Starting to upscale image for filename: {file_name}")
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(model_path)
    sr.setModel("lapsrn",8)
    original_image = cv2.imread(image_path)
    resized_image = cv2.resize(original_image,dsize=None,fx=8,fy=8)
    print(f"Finished upscaling image {file_name}, removing lower resolution version")
    cv2.imwrite(image_path, resized_image)
    print("Completed overwriting original image")
