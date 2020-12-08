# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-client


"""
import logging
import pytest
from unittest.mock import patch
import json
import requests
from requests import Response
import responses

from signal_interpreter_client.interpretation_layer import URL, SIGNAL
from signal_interpreter_client.server_communication_handler import post_message
from signal_interpreter_client.exceptions import SignalInterpreterClientError

logger = logging.getLogger(__name__)


RESP = "My response"
@responses.activate
def test_post_message_with_responses():
    logger.debug("Start of %s function test log.", test_post_message_with_responses.__name__)
    responses.add(
        responses.POST,
        URL,
        json=RESP,
        status=200
    )
    assert post_message(URL, payload={}) == RESP
    logger.debug("End of %s function test log.", test_post_message_with_responses.__name__)


# Why include this in normal tests?
# def test_post_message_withServerOn():
#     '''
#     In this test the post method is not mocked...This test only works when the server is on
#     :return:
#     '''
#     logger.debug("Start of %s function test log.", test_post_message_withServerOn.__name__)
#     try:
#         assert post_message(URL, {SIGNAL: "11"}) == r"ECU Reset"
#         assert post_message(URL, {SIGNAL: "27"}) == r"Security Access"
#     except requests.exceptions.RequestException as error:
#         print("Error: ", error)
#         print("Server is not on. Cannot run this test.")
#     logger.debug("End of %s function test log.", test_post_message_withServerOn.__name__)


# signal does not matter here, could test more but why?
@pytest.mark.parametrize("signal, exceptions", [
    ("11", requests.exceptions.ConnectionError),# Test 1 connection error - user no internet
    ("11", requests.exceptions.Timeout),# Test 2 server not responding - server down
    ("Q", KeyError),# Test 2 if string but not in server - bad request
])
@patch('signal_interpreter_client.server_communication_handler.post')
def test_post_message_width_side_effect(mock_post, signal, exceptions):
    logger.debug("Start of %s function test log.", test_post_message_width_side_effect.__name__)
    mock_post.side_effect = exceptions
    with pytest.raises(SignalInterpreterClientError):
        post_message(URL, {"signal": signal})
    logger.debug("End of %s function test log.", test_post_message_width_side_effect.__name__)
