# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-client


"""


from unittest.mock import patch
import sys

from main import main


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

