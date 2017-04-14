# -*- coding: utf-8 -*-

"""
    tests.t_scripts.test_xobox
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


from importlib.machinery import SourceFileLoader
import os
import sys
from unittest import TestCase, skipIf


class TestScriptsXobox(TestCase):
    """
    Unit tests for ``scripts/xobox.py``
    """

    @skipIf(sys.version_info < (3, 4, 0), "importlib has not yet replaced module `imp` in Python < 3.4")
    def test_01(self):
        """
        Test Case 01:
        Try importing the xobox script (Python>=3.4)
        
        Test is passed if a RuntimeError exception is raised.
        """
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'scripts', 'xobox.py'))
        with self.assertRaises(RuntimeError):
            loader = SourceFileLoader('xobox', path)
            __ = loader.load_module()
