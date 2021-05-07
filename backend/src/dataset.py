import glob
import os


def get_class_names(directory):
    paths = glob.glob(os.path.join(directory, '*'))
    classes = [os.path.basename(os.path.normpath(path)) for path in paths]
    return classes


def get_number_of_classes(directory):
    return len(get_class_names(directory))
