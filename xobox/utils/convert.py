# -*- coding: utf-8 -*-

"""
    xobox.utils.convert
    ~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


from ..conf import get_conf


def to_bytes(value):
    """
    Convert any value into a byte sequence.
    
    :param value: The value to be converted
    :return: Byte sequence
    """
    if isinstance(value, str):
        # noinspection PyArgumentList
        return bytes(source=value, encoding=get_conf('DEFAULT_CHARSET'), errors='replace')
    elif isinstance(value, bytearray):
        return bytes(value)
    elif isinstance(value, bytes):
        return value
    elif value is None:
        return b''
    else:
        # noinspection PyArgumentList
        return bytes(source=str(value), encoding=get_conf('DEFAULT_CHARSET'), errors='replace')


def to_str(value):
    """
    Convert any value into a unicode string.
    
    :param value: The value to be converted
    :return: Resulting string
    """
    if isinstance(value, (bytes, bytearray)):
        return value.decode(encoding=get_conf('DEFAULT_CHARSET'), errors='replace')
    elif value is None:
        return ''
    else:
        return str(value)
