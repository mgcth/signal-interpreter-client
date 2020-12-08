# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-client


"""
import logging
import responses
from unittest.mock import patch
import sys
import contextlib
from io import StringIO

from signal_interpreter_client.interpretation_layer import URL
from signal_interpreter_client.main import main


logger = logging.getLogger(__name__)


RESP = "ECU Reset"
@responses.activate
def test_main():
    responses.add(
        responses.POST,
        URL,
        json=RESP,
        status=200
    )
    temp_stdout = StringIO()
    with contextlib.redirect_stdout(temp_stdout):
        with patch.object(sys, "argv", ["main.main", "--signal", "11"]):
            main()

    output = temp_stdout.getvalue().strip()
    assert output == RESP
