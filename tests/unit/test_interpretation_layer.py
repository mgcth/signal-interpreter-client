# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-client


"""
# pylint: disable=missing-function-docstring
import logging
from unittest.mock import patch
import pytest
from signal_interpreter_client.interpretation_layer import get_interpretation, URL, SIGNAL


logger = logging.getLogger(__name__)


# Use parametrisation here
SIGNAL_RESULT_OK = "OK"


@pytest.mark.parametrize("signal, expected_result", [
    # (888, None),# Test 1 if not string
    ("11", SIGNAL_RESULT_OK)  # Test 2 if string
])
@patch('signal_interpreter_client.interpretation_layer.post_message', return_value=SIGNAL_RESULT_OK)
def test_get_interpretation(mock_post_message, signal, expected_result):
    # Test 1/2
    logger.debug("Start of %s function test log.", test_get_interpretation.__name__)
    assert get_interpretation(signal) == expected_result

    if isinstance(signal, str):
        # Test 2 if string
        mock_post_message.assert_called_with(URL, {SIGNAL: signal})
    logger.debug("End of %s function test log.", test_get_interpretation.__name__)
