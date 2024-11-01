import os

# Directory setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
CONTENT_DIR = os.path.join(IMAGES_DIR, "content")
STYLE_DIR = os.path.join(IMAGES_DIR, "style")
RESULTS_DIR = os.path.join(IMAGES_DIR, "results")

# Model specific style weights
VGG_STYLE_WEIGHTS = {
    "conv1_1": 1,
    "conv2_1": 0.75,
    "conv3_1": 0.2,
    "conv4_1": 0.2,
    "conv5_1": 0.2,
}

ALEXNET_STYLE_WEIGHTS = {
    "conv1": 1,
    "conv2": 0.75,
    "conv3": 0.2,
    "conv4": 0.2,
    "conv5": 0.2,
}
