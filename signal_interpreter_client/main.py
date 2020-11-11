# -*- coding: utf-8 -*-
import argparse
from interprate import get_interpretation
from consts import *

def main():
    args = get_args()
    title = get_interpretation(args.signal)
    print(title)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--{}".format(SIGNAL), required=True)
    return parser.parse_args()

if __name__ == "__main__":
    main()