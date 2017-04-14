# -*- coding: utf-8 -*-

"""
    tests.t_utils.test_termcolor
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


from unittest import TestCase
from xobox.utils.termcolor import supports_color


class TestXoboxUtilsTermColor(TestCase):
    """
    Unit tests for :py:mod:`xobox.utils.termcolor`
    """

    def test_01(self):
        """
        Test Case 01:
        Test return value of :py:func:`~xobox.utils.termcolor.supports_color`.
        
        Test is passed if return value is of type bool.
        """
        return_value = supports_color()
        self.assertIsInstance(return_value, bool)
