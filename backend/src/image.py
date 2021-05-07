from PIL import Image

WIDTH, HEIGHT, CHANNELS = 256, 256, 1
INPUT_SHAPE = (WIDTH, HEIGHT, CHANNELS)


def load_image(path, dimensions=(WIDTH, HEIGHT), channels=CHANNELS):
    print('Loading image {}'.format(path))
    img = Image.open(path)
    img = img.resize(dimensions)
    if img.mode != 'L':
        img = img.convert('L')
    return img
