# -*- coding: utf-8 -*-
"""
DESCRIPTION
* Create a new file which contains a function called get_interpretation and takes signal as input argument and returns
    the JSON-response from the server
* The URL to the server should be moved to get_interpretation as well as the formatting of the payload
* The get_interpretation-function should now be a layer between main() and post_message() and contain all the specifics
    for the Signal Interpreter Server

Created at 2020-11-15
Current project: signal-interpreter-client


"""
from server_communication_handler import post_message

_signal = "signal"
_url = "http://127.0.0.1:5000"


def get_interpretation(signal: str):
    if type(signal) != str:
        return None

    payload = {
        _signal: signal
    }
    return post_message(_url, payload)
