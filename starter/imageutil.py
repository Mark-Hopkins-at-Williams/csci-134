from PIL import Image
import numpy as np


def read_image(filename):
    """Reads an image from the specified file."""
    orig_img = Image.open(filename)
    return np.array(orig_img).tolist()


def read_image_as_grayscale(filename):
    """Reads an image from the specified file and then converts it to grayscale."""
    orig_img = Image.open(filename).convert('L')
    return np.array(orig_img).tolist()


def show_image(image):
    """Displays an image in a pop-up window."""
    array = np.array(image).astype(np.uint8)
    img = Image.fromarray(array)
    img.show()