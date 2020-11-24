# -*- coding: utf-8 -*-
"""
Server message methods.
"""
# server_communication_handler.py
import json
from requests import post


def post_message(url, payload):
    """
    Post message function.
    :param url:
    :param payload:
    :return:
    """
    headers = {"content-type": "application/json"}
    response = post(url, data=json.dumps(payload), headers=headers).json()
    return response
