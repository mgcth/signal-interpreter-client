# -*- coding: utf-8 -*-
import argparse

from interprate import get_interpretation


def main():
    args = get_args()
    title = get_interpretation(args.signal) # args.signal == "11", "27"
    print(title)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--signal", required=True, help='python main.py --signal "your message"')
    return parser.parse_args()


if __name__ == "__main__":
    main()
