# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-client


"""
# pylint: disable=missing-function-docstring
import logging
import sys
from unittest.mock import patch
import contextlib
from io import StringIO
import responses

from signal_interpreter_client.main import main

logger = logging.getLogger(__name__)


@responses.activate
def test_main(responses_add_instance):
    """
    Acceptance criteria
    Add test cases in signal interpreter client which tests the flow from starting the client from main.py to sending a
    POST-request and receiving the correct response
    The integration tests should mock the server and be able to run independently of the signal interpreter server
    Add the possibility to invoke integration tests in tasks.py but do not check the code coverage for integration tests
    :return:
    """
    response = responses_add_instance  # this is the RESPONSE variable

    temporary_print_from_stdout = StringIO()
    with contextlib.redirect_stdout(temporary_print_from_stdout):
        with patch.object(sys, "argv", ["main.main", "--signal", "11"]):
            main()

    output = temporary_print_from_stdout.getvalue().strip()
    assert output == response
