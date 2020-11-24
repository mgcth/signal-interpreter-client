# -*- coding: utf-8 -*-
"""
Client program.
"""
import argparse
# from server_communication_handler import post_message
from signal_interpreter_client.interpretation_layer import get_interpretation


validSignals = ["11", "27"]


def main():
    """
    Entry point to program.
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--{}".format("signal"), required=True)
    args = parser.parse_args()
    signal = args.signal
    if signal in validSignals:
        interp = get_interpretation(signal)
        print(interp)


def init():
    """
    Entry to main.
    :return:
    """
    if __name__ == '__main__':
        main()


init()
