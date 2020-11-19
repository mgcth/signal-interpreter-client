# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-client


"""

from unittest.mock import patch
from interpretation_layer import get_interpretation, URL, SIGNAL


@patch('interpretation_layer.post_message', return_value='OK')
def test_get_interpretation(mock_post_message):
    # Test 1: Only accept string as input:
    assert get_interpretation(888) == None

    # Test 2: Test if the format is ok:
    dummy_sig = "11"
    get_interpretation(dummy_sig)
    mock_post_message.assert_called_with(URL, {SIGNAL: dummy_sig})
