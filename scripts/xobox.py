#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    xobox - Orange Box for X-Plane
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""

import os
import sys


def main():
    """
    xobox main function, acting as central dispatcher 
    """
    # find out if running from an uninstalled version
    # this being the case, insert the appropriate path into PYTHONPATH
    xobox_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    if os.path.isfile(os.path.join(xobox_path, 'xobox', '__init__.py')):
        sys.path.insert(0, xobox_path)

    import xobox.cli
    return xobox.cli.execute()


if __name__ == '__main__':
    sys.exit(main())
else:
    raise RuntimeError("This is an executable file. Do not try to import it!")
    # noinspection PyUnreachableCode
    sys.exit(os.EX_SOFTWARE)
