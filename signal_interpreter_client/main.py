# -*- coding: utf-8 -*-
import argparse
# from server_communication_handler import post_message
from interpretation_layer import get_interpretation

validSignals = ["11", "27"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--{}".format("signal"), required = True)
    args = parser.parse_args()
    signal = args.signal
    if signal in validSignals:
        interp = get_interpretation(signal)
        print(interp)

if __name__ == '__main__':
    main()