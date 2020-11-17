# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-client


"""
from unittest.mock import patch


import json

import requests
from requests import Response

from interpretation_layer import _url, _signal
from server_communication_handler import post_message



@patch('server_communication_handler.post', return_value=Response())
@patch.object(Response, 'json')
def test_post_message(mock_json, mock_post):
    post_message('dummy_url', 'dummy_payload')

    # Test if Response.json() is called
    mock_json.assert_called_once()
    # Test if header is correct
    mock_post.assert_called_with('dummy_url',
                                 data = json.dumps('dummy_payload'),
                                 headers = {"content-type": "application/json"})

def test_post_message_withServerOn():
    '''
    In this test the post method is not mocked...This test only works when the server is on
    :return:
    '''
    try:
        assert post_message(_url, {_signal: "11"}) == r"ECU Reset"
        assert post_message(_url, {_signal: "27"}) == r"Security Access"
    except requests.exceptions.RequestException as error:
        print("Error: ", error)
        print("Server is not on. Cannot run this test.")