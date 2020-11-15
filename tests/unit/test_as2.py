# -*- coding: utf-8 -*-
"""
DESCRIPTION
Acceptance criteria

*Create a new file which contains a function called get_interpretation and takes signal as input argument and returns the
    JSON-response from the server
*The URL to the server should be moved to get_interpretation as well as the formatting of the payload
*The get_interpretation-function should now be a layer between main() and post_message() and contain all the specifics for
    the Signal Interpreter Server
*There should be at least one unit test per function in the production code
*Verify that it works by having a valid signal from the signal database as input to the CLI and see that you get the signal
    title as response from the server (the only signals that are valid are “11” and “27” (as strings))

Message from Roberto:
"So for now, you don't have to mock the built-in functions if you don't want to (e.g. ArgumentParser, jsonify, json.loads etc).
But all the functions that you have written yourself should be mocked if they are being called from the function you are testing."

Created at 2020-11-15
Current project: signal-interpreter-client


"""

from unittest.mock import patch, call
from flask import Flask
import sys

import json

from requests import Response

from interpretation_layer import get_interpretation, _url, _signal
from server_communication_handler import post_message
from main import main

@patch('interpretation_layer.post_message', return_value='OK')
def test_get_interpretation(mock_post_message):
    # Test 1: Only accept string as input:
    assert get_interpretation(888) == None
    # Test 2: Test if the format is ok:
    dummy_sig = "11"
    get_interpretation(dummy_sig)
    mock_post_message.assert_called_with(_url,
                                         {_signal: dummy_sig})


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
    assert post_message(_url, {_signal: "11"}) == r"ECU Reset"
    assert post_message(_url, {_signal: "27"}) == r"Security Access"



@patch('main.get_interpretation')
def test_main(mock_get_interpretation):
    # If the signal is not in the valid signal list, then mock_get_interpretation should not be called
    with patch.object(sys, "argv", ["main.main", "--signal", "8888888"]):
        main()
        assert not mock_get_interpretation.called

    # Test if get_interpretation is called with the CLI input
    with patch.object(sys, "argv", ["main.main", "--signal", "11"]):
        main()
        mock_get_interpretation.assert_called_with("11")


