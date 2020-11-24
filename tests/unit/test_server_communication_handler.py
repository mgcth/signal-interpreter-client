# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-client


"""
import pytest
from unittest.mock import patch
import json
import requests
from requests import Response
import responses

from signal_interpreter_client.interpretation_layer import URL, SIGNAL
from signal_interpreter_client.server_communication_handler import post_message

RESP = "My response"
@responses.activate
def test_post_message_with_responses():
    responses.add(
        responses.POST,
        URL,
        json=RESP,
        status=200
    )
    assert post_message(URL, payload={}) == RESP


@patch('signal_interpreter_client.server_communication_handler.post', side_effect=[requests.exceptions.Timeout])
def test_post_message_width_side_effect(mock_post):
    with pytest.raises(requests.exceptions.Timeout):
        post_message(URL, {"signal": "11"})

    # post_message(URL, 'dummy_payload')
    # # Test if Response.json() is called
    # mock_json.assert_called_once()
    # # Test if header is correct
    # mock_post.assert_called_with(URL,
    #                              data = json.dumps('dummy_payload'),
    #                              headers = {"content-type": "application/json"})


def test_post_message_withServerOn():
    '''
    In this test the post method is not mocked...This test only works when the server is on
    :return:
    '''
    try:
        assert post_message(URL, {SIGNAL: "11"}) == r"ECU Reset"
        assert post_message(URL, {SIGNAL: "27"}) == r"Security Access"
    except requests.exceptions.RequestException as error:
        print("Error: ", error)
        print("Server is not on. Cannot run this test.")