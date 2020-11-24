from unittest.mock import patch, call

from signal_interpreter_client.main import main, init, ArgumentParser, parse_arguments


class MockArguments:
    signal = "11"


@patch.object(ArgumentParser, "parse_args", return_value=MockArguments)
@patch.object(ArgumentParser, "add_argument")
def test_parse_arguments(mock_add_argument, mock_parse_args):
    assert parse_arguments() == MockArguments
    mock_add_argument.assert_called_with("-s", "--signal", required=True, help="signal (e.g. 11)")
    mock_parse_args.assert_called_once()


@patch("builtins.print")
@patch("signal_interpreter_client.main.get_interpretation", return_value="ECU Reset")
@patch("signal_interpreter_client.main.parse_arguments", return_value=MockArguments)
def test_main(mock_parse_arguments, mock_get_interpretation, mock_print):
    main()
    mock_parse_arguments.assert_called_once()
    mock_get_interpretation.assert_called_with(MockArguments.signal)
    mock_print.mock_calls = [call("ECU Reset")]


@patch("signal_interpreter_client.main.main")
@patch("signal_interpreter_client.main.__name__", "__main__")
def test_init(mock_main):
    init()
    mock_main.assert_called_once()
