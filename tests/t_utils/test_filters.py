# -*- coding: utf-8 -*-
"""
    tests.t_utils.test_filters
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2017 by The Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


import os
import importlib
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
        print(test_path)
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
            print(root)
            print(dirs)
            print(files)
            result += list(filter(filters.files, files))
        print(expected)
        print(result)
        expected.sort()
        result.sort()
        print(expected)
        print(result)
        self.assertListEqual(result, expected)

    def test_02(self):
        """
        Test Case 02:
        Detect members of current test module.
        
        Test is passed if the returned list matches with the expected result.
        """
        test_module = importlib.import_module('tests.t_utils.test_filters')
        result = list(filter(filters.members, dir(test_module)))
        expected = ['TestCase', 'TestXoboxUtilsFilters', 'filters', 'importlib', 'os']
        self.assertListEqual(result, expected)

    def test_03(self):
        """
        Test Case 03:
        Detect modules in tests package path.
        
        Test is passed if the returned list matches with the expected result.
        """
        test_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        gen_dir = os.listdir(test_path)
        result = list(filter(filters.modules, gen_dir))
        expected = ['t_cli', 't_conf', 't_core', 't_scripts', 't_utils', 'test_xobox.py']
        self.assertListEqual(result, expected)
