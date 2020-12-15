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
import logging
from signal_interpreter_client.server_communication_handler import post_message

logger = logging.getLogger(__name__)

SIGNAL = "signal"
URL = "http://127.0.0.1:5000"


def get_interpretation(signal: str):
    """
    Interpreter function.
    :param signal:
    :return:
    """
    # removed test for str here because we do it with try except block in post_message
    # test is unchanged, but one less case used
    payload = {
        SIGNAL: signal
    }
    logger.info("Payload ready to be sent %s.", payload)
    return post_message(URL, payload)
