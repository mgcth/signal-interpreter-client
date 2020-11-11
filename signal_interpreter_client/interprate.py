from server_communication_handler import post_message
from consts import *

def get_interpretation(signal):
    payload = { SIGNAL: signal }
    title = post_message(URL, payload)
    return title