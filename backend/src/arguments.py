import argparse


def _setup_parser():
    parser = argparse.ArgumentParser(description='Classifier for mushrooms')
    parser.add_argument('--train', dest='mode', action='store_true')
    parser.add_argument('--classify', dest='mode', action='store_false')
    parser.add_argument('--marketplace', type=str, required=True)
    parser.add_argument('--model', type=str)
    return parser


def get_args():
    return _setup_parser().parse_args()
