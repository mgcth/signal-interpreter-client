"""
Share the post message between tests.
"""
# conftest.py
import pytest
import responses

from signal_interpreter_client.interpretation_layer import URL


RESPONSE = "ECU Reset"


@pytest.fixture
def responses_add_instance():
    """
    Do as post to server.
    :return:
    """
    responses.add(
        responses.POST,
        URL,
        json=RESPONSE,
        status=200
    )
    # return the response to get this in the tests and not have to hard-code the RESPONSE variable there
    # this function then also has side-effects
    return RESPONSE
