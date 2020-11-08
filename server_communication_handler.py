# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created by CWENG at 2020-11-04
Current project: VeldiPython


"""
import json
from requests import post



def post_message(url, payload):
    headers = {"content-type": "application/json"}
    response = post(url, data=json.dumps(payload), headers=headers)
    return response.json()

