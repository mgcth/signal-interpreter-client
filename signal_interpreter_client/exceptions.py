"""
Custom Exceptions.
"""


class SignalInterpreterClientError(Exception):
    """
    No signal error.
    The custom exception could for example be called SignalInterpreterClientError and be used for wrapping other
    exceptions such as ConnectionError or when the user has entered a signal that is not part of the signal database file
    """
