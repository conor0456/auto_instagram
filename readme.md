# Auto Instagram
## Setup
```
git clone git@github.com/auto_instagram.git
cd auto_instagram
./init.sh
```
## Summary
This application is designed to be copied to a server and ran periodically with `cron`. The application generates content using OpenAI's models and publishes the result to Instagram. For an example of what the application is capable of you can view a sample Instagram page [here](https://www.instagram.com/rothkoauto/).

##### Key Data Models
|Data Model   |Description                              |
|:--------------------------|:---------------------------|
| `Subject` |  A `subject` is the focus of an individual application run. It should be a proper noun like `Jackson Pollock` or `Frank Lloyd Wright` |
| `Prompt` |  A `prompt` is a key concept in OpenAI's generative models. The prompt is used to generate text or images, you can learn more about them [here](https://beta.openai.com/docs/guides/completion/prompt-design) |
| `Persistence` |  After generating the image we can choose to `persist` the image either locally or to Google Drive |
| `Caption` |  The `caption` is constructed in the `build_caption` method of the `instagram/helper` module and attached to the image prior to publishing the image to Instagram |

##### Application Modules
|Module   |Description                              |
|:--------------------------|:---------------------------|
| `image_upscaling` | Currently OpenAI only generates images up to a `1080x1080` resolution. The `image_upscaling` package offers the `cv2_client` module which enables upscaling of the images to 4k  |
| `instagram` | The `instagram` package contains the `client` module for publishing images to Instagram as well as a `helper` module which contains methods useful in generating the Instagram post   |
| `lib` | The `lib` package contains the `utils` module for all miscellaneous methods useful to the application  |
| `open_ai` | The `open_ai` package contains the `client` module which offers all of the methods for generating prompts and images using OpenAI's capabilities |
| `persistence` | The `persistence` package contains the `google_drive_client` module for storing images to Google Drive as well as the `local_storage` module for storing images locally on disk  |
| `subject_generator` | The `subject_generator` package contains the list of subjects to pull from in `subjects.csv` and the `generate_subject` module for randomly picking a subject from the list  |

##### Application Steps
This application runs the following steps in the `auto_instagram/run.py` file
1. Select a random subject from the `subjects.csv` file
2. Generate a prompt that will be used to generate an image
3. Generate a summary of the subject
4. Generate a title for the image
5. Generate the image and save it locally
6. Build caption for the Instagram post
7. Save the caption, title, and file name to the local `generated_results.csv` file
8. (Optional) Post the image and caption to Instagram
9. (Optional) Upscale the image to 4k
10. (Optional) Save image remotely
11. (Optional) Delete local image

## Credentials
There are three sources of credentials you will need to run this script:
1. [Open AI](https://beta.openai.com/docs/api-reference/authentication)
2. [Facebook](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/)
3. [Google Drive](https://developers.google.com/drive/api/guides/api-specific-auth)

Credentials must be stored in an environment config file named `.env` following the example provided in `.env_example`

|Configuration Key   |Description            |Requied |
|:--------------------------|:---------------------------|:------|
| `OPEN_AI_TOKEN` |  Oauth token generated with developer account | `True` |
| `INSTAGRAM_CLIENT_ID` |  Facebook Application ID | `True` |
| `INSTAGRAM_CLIENT_SECRET` |  Facebook Application secret | `True` |
| `INSTAGRAM_USER_ID` |  Instagram business account ID | `True` |
| `INSTAGRAM_GENERATED_TOKEN` |  Long living auth token for user | `True` |
| `GOOGLE_DRIVE_CLIENT_ID` |  Google oauth client id | `False` |
| `GOOGLE_DRIVE_CLIENT_SECRET` |  Google oauth client secret | `False` |
| `GOOGLE_DRIVE_CLIENT_REFRESH_TOKEN` |  Google oauth client long living token | `False` |

Facebook tokens last at most 60 days before expiration. Unfortunately there is no current mechanism for refreshing the oauth token without input from the user. To generate a new `INSTAGRAM_GENERATED_TOKEN` token, first fetch an oauth token from your facebook application and exchange it with the `exchange_short_token_for_long_token` method in the `instagram/client` module. This will open a page that will prompt you to log in to your Facebook developer account.

## Generic Configuration Settings
Within the same `.env` file you can control the application settings

|Configuration Key   |Description            |Requied |
|:--------------------------|:---------------------------|:------|
| `GENERATIVE_TEXT_ENGINE` |  Which OpenAI model to use for prompt generation. Learn more about the models [here](https://beta.openai.com/docs/models/gpt-3) | `True` |
| `IMAGE_PROMPT_GENERATION_PROMPT` |  The prompt sent to generate the prompt the application will use to build the image. Use `{SUBJECT}` to interpolate the `Subject` into the prompt  | `True` |
| `SUMMARY_GENERATION_PROMPT` |  The prompt used to generate the summary of the subject. Use `{SUBJECT}` to interpolate the `Subject` into the prompt | `True` |
| `TITLE_GENERATION_PROMPT` |  The prompt used to generate the title of the image. Use `{SUBJECT}` to interpolate the `Subject` and `{IMAGE_GENERATION_PROMPT}` to interpolate the `image generation prompt` into the prompt | `True` |
| `GOOGLE_DRIVE_IMAGE_DIRECTORY_ID` |  Path within google drive in which to save the generated images. Navigate to the folder in Google Drive and pull the id from the URL | `False` |
| `RESAMPLING_LOOKBACK_THRESHOLD` | Exclude `N` previously generated `subjects` from the list of eligible `subjects` that can be sampled from. Setting this value to `0` will result in resampling with no threshold | `False` |


## Runtime Configuration Settings
Additionally, you can control individual application runs with the following settings. If not defined, the configurations will default to `False`

|Configuration Key   |Description            |Requied |
|:--------------------------|:---------------------------|:------|
| `POST_TO_INSTAGRAM` |  Whether the application should post the result to Instagram | `False` |
| `UPSCALE_IMAGE` |  Whether the application should upscale the image to 4k | `False` |
| `PERSIST_IMAGES_LOCALLY` |  Whether the application should save the image locally | `False` |
| `PERSIST_IMAGES_REMOTELY` |  Whether the application should save the image remotely | `False` |


These runtime configs can also be passed in when running the script

|Argument   |Shorthand            |Full Argument |
|:--------------------------|:---------------------------|:------|
| `POST_TO_INSTAGRAM` |  `-p` | `--post_to_instagram` |
| `UPSCALE_IMAGE` |  `-u` | `--upscale_image` |
| `PERSIST_IMAGES_LOCALLY` |  `-l` | `--store_locally` |
| `PERSIST_IMAGES_REMOTELY` |  `-r` | `--store_remotely` |


## Example Uses
```
# Generate the image and save it to Google Drive but do not post to instagram:
python auto_instagram/run.py -p False -r True

# Generate the image, upscale it, and post it to Instagram without saving the image to Google Drive or locally
python auto_instagram/run.py -p True -u True -l False -r False
```
