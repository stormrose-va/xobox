# -*- coding: utf-8 -*-
"""
    tests.t_utils.test_filters
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2017 by The Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


import os
from unittest import TestCase
from xobox.utils import filters


class TestXoboxUtilsFilters(TestCase):
    """
    Unit tests for :py:mod:`xobox.utils.filters`
    """

    def test_01(self):
        """
        Test Case 01:
        Detect test modules in current path.
        
        Test is passed if the returned list matches with the expected result.
        """
        test_path = os.path.dirname(os.path.realpath(__file__))
        result = []
        expected = [
            'test_compat.py',
            'test_convert.py',
            'test_dynamic.py',
            'test_filters.py',
            'test_loader.py',
            'test_singleton.py',
            'test_termcolor.py',
            'test_timer.py',
            'test_version.py'
        ]
        for root, dirs, files in os.walk(test_path):
            result += list(filter(filters.files, files))
        self.assertListEqual(result, expected)
