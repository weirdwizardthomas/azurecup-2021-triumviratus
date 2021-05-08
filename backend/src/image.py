from PIL import Image

import config

WIDTH, HEIGHT, CHANNELS = config.to_tuple(config.config.image)
INPUT_SHAPE = (WIDTH, HEIGHT, CHANNELS)


def load_image(path, dimensions=(WIDTH, HEIGHT), channels=CHANNELS):
    """
    Loads images with desired dimensions and colour channels.
    :param path: Path to the image.
    :param dimensions: Required width x height.
    :param channels: Required number of channels (currently not in use, all images are required to be greyscale)
    :return: PIL.Image of the formatted image.
    """
    print('Loading image {}'.format(path))
    img = Image.open(path)
    img = img.resize(dimensions)
    if img.mode != 'L':
        img = img.convert('L')
    return img
