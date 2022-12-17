import open_ai.client as ai_client
import instagram.helper as helper
import instagram.client as instagram_client
import prompt_generator.generate_artist as artist_generator
import image_upscaling.cv2_client as upscaler
import persistence.local_storage as local_storage
import persistence.google_drive_client as google_storage
import lib.utils as utils

utils.print_run_configs()

subject = artist_generator.fetch_random_artist()
image_generation_prompt = ai_client.generate_image_generation_prompt(subject)
file_name = ai_client.generate_file_name(image_generation_prompt, subject)
summary = ai_client.generate_subject_summary(subject)
title = ai_client.generate_image_title(image_generation_prompt)
image_url = ai_client.generate_and_save_image(image_generation_prompt, subject)
instagram_caption = helper.build_caption(title, image_generation_prompt, summary)
local_storage.save_content(subject, title, summary, file_name)

if utils.should_post_to_instagram():
    instagram_client.post_file_to_instagram_with_caption(image_url, instagram_caption)

if utils.should_upscale_image():
    upscaler.upscale_and_overwrite_image(file_name)

if utils.should_persist_image_remotely():
    google_storage.upload_file_to_drive(file_name)

if not utils.should_persist_image_locally():
    print(f"PERSIST LOCALLY: {utils.should_persist_image_locally()}")
    utils.clean_up_local_image(file_name)

print(f"Completed all tasks")
