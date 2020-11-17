import sys
from unittest.mock import patch, call
from argparse import Namespace
from consts import *
from main import get_args, main
from interprate import get_interpretation
from server_communication_handler import post_message


@patch("interprate.post_message")
def test_get_interpretation_test(mock_post_message):
    test = "TEST"
    mock_post_message.return_value = test
    assert get_interpretation("11") == test
    assert get_interpretation("27") == test


@patch("server_communication_handler.post")
def test_post_message_test(mock_post):
    payload = {"signal": "11"}
    mock_post.return_value.json.return_value = payload
    assert post_message(URL, payload) == payload


@patch.object(sys, "argv", ["signal-interpreter-client", "--signal", "11"])
def test_get_args_test():
     assert get_args() == Namespace(signal="11")


@patch("builtins.print")
@patch("main.get_interpretation")
@patch("main.get_args")
def test_main_test(mock_get_args, mock_get_interpretation, mock_print):
    signal = "11"
    args = {"signal": signal}
    mock_get_args.return_value = args
    mock_get_interpretation.return_value = signal

    main()
    mock_get_interpretation.assert_called_with("11")
    assert mock_print.mock_calls == [call('11')]
