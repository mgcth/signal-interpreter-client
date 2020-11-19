# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-client


"""
import pytest
from unittest.mock import patch
from signal_interpreter_client.interpretation_layer import get_interpretation, URL, SIGNAL

# Use parametrisation here
OK = "OK"
@pytest.mark.parametrize("signal, expected_result", [
    (888, None),# Test 1 if not string
    ("11", OK)# Test 2 if string
])
@patch('signal_interpreter_client.interpretation_layer.post_message', return_value=OK)
def test_get_interpretation(mock_post_message, signal, expected_result):
    # Test 1/2
    assert get_interpretation(signal) == expected_result

    if isinstance(signal, str):
        # Test 2 if string
        mock_post_message.assert_called_with(URL, {SIGNAL: signal})
