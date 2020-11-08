# -*- coding: utf-8 -*-
import argparse
from server_communication_handler import post_message

signal = "signal"
parser = argparse.ArgumentParser()
parser.add_argument("--{}".format(signal), required = True)
args = parser.parse_args()

payload = {
    signal: args.signal
}

post_message("http://127.0.0.1:5000", payload)