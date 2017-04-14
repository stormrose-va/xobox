# -*- coding: utf-8 -*-

"""
    tests.t_utils.test_timer
    ~~~~~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


from unittest import TestCase
from xobox.utils.timer import counter


class TestXoboxUtilsTimer(TestCase):
    """
    Unit tests for :py:mod:`xobox.utils.timer`
    """

    def test_01(self):
        """
        Test Case 01:
        Test return type of :py:func:`~xobox.utils.timer.counter`.
        
        Test is passed if returned value is of type float.
        """
        self.assertIsInstance(counter(), float)

    def test_02(self):
        """
        Test Case 02:
        Test result of two subsequent calls of :py:func:`~xobox.utils.timer.counter`.
        
        Test is passed if result of second call is greater than result of first call.
        """
        r1 = counter()
        r2 = counter()
        self.assertGreater(r2, r1)
