"""Shared inner functionalities for pdpipe."""

import inspect
import numpy as np


def _interpret_columns_param(columns):
    if isinstance(columns, str):
        return [columns]
    if hasattr(columns, '__iter__'):
        return columns
    return [columns]


def _list_str(listi):
    if listi is None:
        return None
    if isinstance(listi, (list, tuple)):
        return ', '.join([str(elem) for elem in listi])
    return listi


def _get_args_list(func):
    signature = inspect.signature(func)
    return list(signature.parameters.keys())


def _identity_function(x):
    return x


def _str2list(s):
    if type(s) == str:
        return [s]
    elif isinstance(s, (list, np.ndarray, tuple)):
        return s
