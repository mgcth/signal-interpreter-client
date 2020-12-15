# -*- coding: utf-8 -*-
"""
Client program.
"""
import logging
import argparse
from signal_interpreter_client.interpretation_layer import get_interpretation

logger = logging.getLogger(__name__)

validSignals = ["11", "27"]


def get_signal_from_arguments():
    """
    Parse arguments.
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--{}".format("signal"), required=True)
    arguments = parser.parse_args()
    return arguments.signal


def main():
    """
    Entry point to program.
    :return:
    """
    logger.info("Program started.")
    signal = get_signal_from_arguments()
    logger.info("Entered signal request: %s", signal)
    interp = get_interpretation(signal)
    logger.info("Received title: %s", interp)
    print(interp)
    logger.info("Program terminated.")


def init():
    """
    Entry to main.
    :return:
    """
    if __name__ == '__main__':
        main()


init()
