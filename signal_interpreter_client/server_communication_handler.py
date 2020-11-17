# -*- coding: utf-8 -*-
# server_communication_handler.py
import json
from requests import post


def post_message(url, payload):
    headers = {"content-type": "application/json"}
    response = post(url, data=json.dumps(payload), headers=headers).json()
    return response

