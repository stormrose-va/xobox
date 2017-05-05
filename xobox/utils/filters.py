# -*- coding: utf-8 -*-
"""
    xobox.utils.filter
    ~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2017 by The Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


import os
import re


def files(item):
    """
    Filter for Python modules beginning with *test_*
    
    :param str item: the item to be tested with this filter
    """
    file, ext = os.path.splitext(item)
    if file != '__init__' and ext == '.py' and file[:5] == 'test_':
        return True
    return False


def members(item):
    """
    Filter function to detect classes within a module or package

    :param str item: the item to be tested with this filter
    """
    exclude = (
        re.escape('__all__'),
        re.escape('__builtins__'),
        re.escape('__cached__'),
        re.escape('__doc__'),
        re.escape('__file__'),
        re.escape('__loader__'),
        re.escape('__name__'),
        re.escape('__package__'),
        re.escape('__path__'),
        re.escape('__spec__')
    )
    pattern = re.compile('|'.join(exclude))
    return not pattern.search(item)


def modules(item):
    """
    Filter function to detect processor modules and packages

    :param str item: the item to be tested with this filter
    """
    exclude = (
        re.escape('__init__.py'),
    )
    pattern = re.compile('|'.join(exclude))
    return not pattern.search(item)
