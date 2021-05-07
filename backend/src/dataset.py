import glob
import os


def get_class_names(directory):
    """
    Provides name of image classes in a directory.
    :param directory: Directory containing classes.
    :return: List of classes
    """
    paths = glob.glob(os.path.join(directory, '*'))
    classes = [os.path.basename(os.path.normpath(path)) for path in paths]
    return classes


def get_number_of_classes(directory):
    """
    Provides the count of image classes in a directory.
    :param directory: Directory containing classes.
    :return: int. Number of classes in a directory
    """
    return len(get_class_names(directory))
