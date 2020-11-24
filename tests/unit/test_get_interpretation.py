from unittest.mock import patch

from signal_interpreter_client.get_interpretation import get_interpretation


def test_get_interpretation():
    with patch("signal_interpreter_client.get_interpretation.post_message") as mock_post_message:
        get_interpretation("11")
        mock_post_message.assert_called_with("http://127.0.0.1:5000/", {"signal": "11"})
