import argparse
import sys

CLASSIFY = '--classify'
TRAIN = '--train'


def _setup_parser():
    """
    Configures a parser.
    :return: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description='Classifier for mushrooms')
    parser.add_argument(TRAIN, dest='mode', action='store_true')
    parser.add_argument(CLASSIFY, dest='mode', action='store_false')
    parser.add_argument('--marketplace', type=str, required=CLASSIFY in sys.argv)
    parser.add_argument('--model', type=str, required=CLASSIFY in sys.argv)
    parser.add_argument('--train-data', type=str, required=TRAIN in sys.argv)
    parser.add_argument('--test-data', type=str, required=TRAIN in sys.argv)
    parser.add_argument('--classes', type=str, required=CLASSIFY in sys.argv)
    return parser


def get_args():
    """
    Provides command-line arguments
    :return: argparse.Namespace. Command-line arguments
    """
    return _setup_parser().parse_args()
