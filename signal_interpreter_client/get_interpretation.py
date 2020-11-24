"""
Interpret the signal.
"""
from signal_interpreter_client.server_communication_handler import post_message


def get_interpretation(signal):
    """
    Send message to the server_communication handler
    :return:
    """
    url = r"http://127.0.0.1:5000/"
    payload = {"signal": signal}
    return post_message(url, payload)
