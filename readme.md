# Auto Instagram
## Getting Started
```
git clone git@github.com/auto_instagram.git
cd auto_instagram
./init.sh
```

Next, add an environment config file following the example provided in `.env_example`

Use the following flags to control how the script runs
```
To control whether the image is posted to Instagram
POST_TO_INSTAGRAM=False

To control whether to upscale the image to 4k
UPSCALE_IMAGE=True

To save the image locally
PERSIST_IMAGES_LOCALLY=True

To save the image to a remote
PERSIST_IMAGES_REMOTELY=True
```
