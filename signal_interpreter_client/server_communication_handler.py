# -*- coding: utf-8 -*-
"""
Server message methods.
"""
import logging
import json
from requests import post, exceptions
from signal_interpreter_client.exceptions import SignalInterpreterClientError


logger = logging.getLogger(__name__)


def post_message(url, payload):
    """
    Post message function.
    :param url:
    :param payload:
    :return:
    """
    headers = {"content-type": "application/json"}
    try:
        logger.info("Posting message to server.")
        server_resp = post(url, data=json.dumps(payload), headers=headers)
        server_resp.raise_for_status()
        response = server_resp.json()
        logger.info("Response received %s.", response)
        return response
    except exceptions.Timeout as err:
        logger.exception("Exception occurred in POST: %s", err)
        raise SignalInterpreterClientError from err
    except KeyError as err:
        logger.exception("Exception occurred in POST: %s", err)
        raise SignalInterpreterClientError from err
    except exceptions.ConnectionError as err:
        logger.exception("Exception occurred in POST: %s", err)
        raise SignalInterpreterClientError from err
