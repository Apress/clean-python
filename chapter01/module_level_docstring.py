"""This module contains all the network related request.

This module will check for all the exceptions while making the network calls
and raise exceptions for any unknown exception. Make sure that when you use
this module, you handle these exceptions in client code as:
        NetworkError exception for network calls.
        NetworkNotFound exception if network not found.
"""


import urllib3
import json
