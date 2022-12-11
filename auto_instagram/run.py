import open_ai.client as ai_client
import instagram.helper as helper
import instagram.client as instagram_client
import prompt_generator.generate_artist as artist_generator

subject = artist_generator.fetch_random_artist()
image_generation_prompt = ai_client.generate_image_generation_prompt(subject)
summary = ai_client.generate_subject_summary(subject)
title = ai_client.generate_image_title(image_generation_prompt)
image_url = ai_client.generate_and_save_image(image_generation_prompt, subject)
instagram_caption = helper.build_caption(title, image_generation_prompt, summary)
instagram_client.post_file_to_instagram_with_caption(image_url, instagram_caption)

print(f"Completed task, wrote the following caption: {instagram_caption}")
