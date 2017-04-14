# -*- coding: utf-8 -*-

"""
    xobox
    ~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


#: Official version quintuple for the :py:mod:`xobox` package
VERSION = (0, 1, 0, 'alpha', 0)

#: Official copyright information for the :py:mod:`xobox` package
COPYRIGHT = ('2017', 'the Stormrose Project team')


def get_version(*args, **kwargs):
    """
    Function providing the official version information for a xobox installation.
    
    Currently, this is a mirror of :py:func:`xobox.utils.version.get_version`,
    provided for convenience, e. g. for easier use in a setup script or similar.
    
    .. warning::
       Since the implementation of this function may change in the future, always
       use *this* function and not :py:func:`xobox.utils.version.get_version`
       when retrieving official version information.
    """
    from .utils.version import get_version
    return get_version(*args, **kwargs)


def get_development_status(*args, **kwargs):
    """
    Function providing the official development status for a xobox installation.
    
    Currently, this is a mirror of :py:func:`xobox.utils.version.get_development_status`,
    provided for convenience, e. g. for easier use in a setup script or similar.
    
    .. warning::
       Since the implementation of this function may change in the future, always
       use *this* function and not :py:func:`xobox.utils.version.get_development_status`
       when retrieving official development status information.
    """
    from .utils.version import get_development_status
    return get_development_status(*args, **kwargs)
