# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-client


"""
from unittest.mock import patch
import logging
import sys
import contextlib
from io import StringIO

from signal_interpreter_client.main import main, init

logger = logging.getLogger(__name__)


@patch("signal_interpreter_client.main.main")
@patch("signal_interpreter_client.main.__name__", "__main__")
def test_init(mock_main):
    logger.debug("Start of %s function test log.", test_init.__name__)
    init()
    mock_main.assert_called_once()
    logger.debug("End of %s function test log.", test_init.__name__)


RESP = "ECU Reset"


@patch('signal_interpreter_client.main.get_interpretation')
def test_main(mock_get_interpretation):
    logger.debug("Start of %s function test log.", test_main.__name__)
    mock_get_interpretation.return_value = RESP
    temp_stdout = StringIO()
    with contextlib.redirect_stdout(temp_stdout):
        with patch.object(sys, "argv", ["main.main", "--signal", "11"]):
            main()
            mock_get_interpretation.assert_called_with("11")

    output = temp_stdout.getvalue().strip()
    assert output == RESP
    logger.debug("End of %s function test log.", test_main.__name__)
