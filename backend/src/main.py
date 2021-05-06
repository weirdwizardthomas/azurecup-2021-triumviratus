import os

from src import arguments, responder, watcher

INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'


def configurate(args):
    responder.Responder.directory = os.path.join(args.marketplace, OUTPUT_FOLDER)
    watcher.Watcher.directory = os.path.join(args.marketplace, INPUT_FOLDER)


def train():
    ...


if __name__ == '__main__':
    args = arguments.get_args()

    if args.mode:
        configurate(args)
        w = watcher.Watcher(args.model)
        w.run()
    else:
        train()
