# -*- coding: utf-8 -*-
"""
    xobox.cli
    ~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


from .dispatch import CommandDispatcher


def execute(argv=None):
    """
    Function being called from the executable to launch the CLI.
    This is the initial entrance point for any xobox processing.
    Usually, this function is invoked by an executable Python script
    to start the actual xobox CLI process. This could look like the
    following example::
    
       import sys
       from xobox.cli import execute
       sys.exit(execute(sys.argv))
       
    :param list argv: list of (command line) arguments
    """
    dispatcher = CommandDispatcher(argv)
    dispatcher.execute()
    return dispatcher.status
