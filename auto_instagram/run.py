import open_ai.client as ai_client

subject = 'Willem de Kooning'
image_generation_prompt = ai_client.generate_image_generation_prompt(subject)
summary = ai_client.generate_subject_summary(subject)
ai_client.generate_and_save_image(image_generation_prompt, subject)

print(f"Summary: {summary}")
