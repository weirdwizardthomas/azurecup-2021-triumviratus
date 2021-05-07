import argparse
import sys

CLASSIFY = '--classify'
TRAIN = '--train'


def _setup_parser():
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
    return _setup_parser().parse_args()
