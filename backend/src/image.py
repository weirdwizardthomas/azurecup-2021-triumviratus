from PIL import Image

import config
import template

WIDTH, HEIGHT, CHANNELS = config.to_tuple(config.config.image)
INPUT_SHAPE = (WIDTH, HEIGHT, CHANNELS)


def load_image(path, dimensions=(WIDTH, HEIGHT)):
    """
    Loads images with desired dimensions and colour channels.
    :param path: Path to the image.
    :param dimensions: Required width x height.
    :return: PIL.Image of the formatted image.
    """
    print(template.LOADING_IMAGE.format(path))
    img = Image.open(path)
    img = img.resize(dimensions)
    if img.mode != 'L':
        img = img.convert('L')
    return img
