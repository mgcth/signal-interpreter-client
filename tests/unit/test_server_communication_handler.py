import pytest
from unittest.mock import patch
import json
import requests
from requests import Response
import responses

from signal_interpreter_client.server_communication_handler import post_message


@patch("signal_interpreter_client.server_communication_handler.post")
def test_post_works(mock_post):
    url = "http://127.0.0.1:5000/"
    payload = {"signal": "27"}
    headers = {"content-type": "application/json"}
    post_message(url, payload)
    mock_post.assert_called_with(url, data=json.dumps(payload), headers=headers)


@responses.activate
def test_post_message_with_responses():
    responses.add(
        responses.POST,
        "http://127.0.0.1:5000/",
        json="My response",
        status=200
    )
    assert post_message("http://127.0.0.1:5000/", payload={}) == "My response"


@patch('signal_interpreter_client.server_communication_handler.post', side_effect=[requests.exceptions.Timeout])
def test_post_message_width_side_effect(mock_post):
    with pytest.raises(requests.exceptions.Timeout):
        post_message("http://127.0.0.1:5000/", {"signal": "11"})

