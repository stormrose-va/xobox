# -*- coding: utf-8 -*-

"""
    xobox.conf.default
    ~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


import os
import appdirs
import xobox


# This file contains all default settings used anywhere in the xobox code.
# As a matter of principle, all settings can be overridden (where it makes
# sense).
#
# Please note:
# As a convention, all default setting designators have to be typed
# in capital letters.


# CORE Settings
###############

#: Default character set to be used for any byte sequence or string conversion operations
import sys

#: Default character set to be used for any byte sequence or string conversion operations
DEFAULT_CHARSET = 'utf-8'

#: Default :py:mod:`pickle` protocol to be used
DEFAULT_PICKLE_PROTOCOL = 2

#: Default xobox Executable
DEFAULT_XOBOX_EXECUTABLE = os.path.basename(sys.argv[0])

#: Default configuration file name
DEFAULT_CONF_FILE = os.path.join(
    appdirs.user_config_dir(appname=xobox.get_app_name(), appauthor=xobox.get_app_author()),
    'xobox.ini'
)

#: Default configuration section for core options
DEFAULT_CONF_SECT_CORE = 'core'

#: Default configuration section for core options
DEFAULT_CONF_SECT_LOG = 'log'


# LOGGING
#########

#: Default log type
DEFAULT_LOG_TYPE = 'term'

#: Default log level
DEFAULT_LOG_LEVEL = 'notice'

#: Default log file
DEFAULT_LOG_FILE = os.path.join(
    appdirs.user_log_dir(appname=xobox.get_app_name(), appauthor=xobox.get_app_author(), opinion=False),
    'xobox.log'
)

#: Default timestamp format for file logging
DEFAULT_LOG_TIMESTAMP = '%Y-%m-%d %H:%M:%S'

#: By default, use colors for logging where available
DEFAULT_LOG_COLOR = True
