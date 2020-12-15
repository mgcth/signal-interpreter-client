# -*- coding: utf-8 -*-
"""
Client program.
"""
import logging
import argparse
from signal_interpreter_client.interpretation_layer import get_interpretation

logger = logging.getLogger(__name__)

validSignals = ["11", "27"]


def main():
    """
    Entry point to program.
    :return:
    """
    logger.info("Program started.")
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--{}".format("signal"), required=True)
    args = parser.parse_args()
    signal = args.signal
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
