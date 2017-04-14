# -*- coding: utf-8 -*-

"""
    tests.t_utils.test_compat
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


import os
from unittest import TestCase


class TestXoboxUtilsCompat(TestCase):
    """
    Unit tests for :py:mod:`xobox.utils.compat`
    """

    def test_01(self):
        """
        Test Case 01:
        Verify EX_OK is provided
        
        Test is passed if no exception is raised.
        """
        flag = True
        try:
            from xobox.utils.compat import EX_OK
        except ImportError:
            flag = False

        self.assertTrue(flag)

    def test_02(self):
        """
        Test Case 02:
        Verify EX_UNAVAILABLE is provided

        Test is passed if no exception is raised.
        """
        flag = True
        try:
            from xobox.utils.compat import EX_UNAVAILABLE
        except ImportError:
            flag = False

        self.assertTrue(flag)

    def test_03(self):
        """
        Test Case 03:
        Verify EX_USAGE is provided

        Test is passed if no exception is raised.
        """
        flag = True
        try:
            from xobox.utils.compat import EX_USAGE
        except ImportError:
            flag = False

        self.assertTrue(flag)
