# server_communication_handler.py Lec1-Afzal-as2
import json
from requests import post


def post_message(url, payload):
    headers = {"content-type": "application/json"}
    response = post(url, data=json.dumps(payload), headers=headers)
    return response.json()


# post_message("http://127.0.0.1:5000", {"signal": "it is a cold day"})
