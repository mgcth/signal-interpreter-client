# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-client


"""
# pylint: disable=missing-function-docstring
from unittest.mock import patch
import logging
import sys
import contextlib
from io import StringIO

from signal_interpreter_client.main import main, init, get_signal_from_arguments


logger = logging.getLogger(__name__)


@patch("signal_interpreter_client.main.main")
@patch("signal_interpreter_client.main.__name__", "__main__")
def test_init(mock_main):
    logger.debug("Start of %s function test log.", test_init.__name__)
    init()
    mock_main.assert_called_once()
    logger.debug("End of %s function test log.", test_init.__name__)


RESPONSE = "ECU Reset"
SIGNAL = "11"


@patch.object(sys, "argv", ["signal-interpreter-client", "-s", SIGNAL])
def test_get_signal_from_arguments():
    """
    Test the argument parser.
    :return:
    """
    assert get_signal_from_arguments() == SIGNAL


@patch("signal_interpreter_client.main.get_signal_from_arguments")
@patch('signal_interpreter_client.main.get_interpretation')
def test_main(mock_get_interpretation, mock_get_signal_from_arguments):
    logger.debug("Start of %s function test log.", test_main.__name__)
    # If the signal is not in the valid signal list, then mock_get_interpretation should not be called
    # Again moved this to post_message - so propagate bad signal all the way until server responds
    # with patch.object(sys, "argv", ["main.main", "--signal", "8888888"]):
    #    main()
    #    assert not mock_get_interpretation.called

    mock_get_signal_from_arguments.return_value = SIGNAL

    # Test if get_interpretation is called with the CLI input
    mock_get_interpretation.return_value = RESPONSE
    temp_stdout = StringIO()
    with contextlib.redirect_stdout(temp_stdout):
        main()
        mock_get_interpretation.assert_called_with(SIGNAL)
        output = temp_stdout.getvalue().strip()
        assert output == RESPONSE
    logger.debug("End of %s function test log.", test_main.__name__)
