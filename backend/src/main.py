import os

import arguments
import publisher
import watcher
from src import dataset

INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'


def configure(args):
    publisher.Publisher.directory = os.path.join(args.marketplace, OUTPUT_FOLDER)
    watcher.Watcher.directory = os.path.join(args.marketplace, INPUT_FOLDER)


def train():
    ...  # todo


if __name__ == '__main__':
    args = arguments.get_args()

    if args.mode:
        train()
    else:
        configure(args)
        # todo before starting get all files in directory and run classification on them
        w = watcher.Watcher(args.model, dataset.get_class_names(args.classes))
        w.run()
