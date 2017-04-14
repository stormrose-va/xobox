# -*- coding: utf-8 -*-

"""
    tests.t_utils.test_dynamic
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


from unittest import TestCase
from xobox.utils.dynamic import Dynamic, DynamicIterable


class TestXoboxUtilsDynamic(TestCase):
    """
    Unit tests for :py:mod:`xobox.utils.dynamic`
    """

    def test_01(self):
        """
        Test Case 01:
        Try instantiating a Dynamic object.
        
        Test is passed if the instance proves being a :py:class:`~xobox.utils.dynamic.Dynamic` instance.
        """
        obj = Dynamic()
        self.assertIsInstance(obj, Dynamic)

    def test_02(self):
        """
        Test Case 02:
        Instantiate a dynamic object with payload data.
        
        Test is passed if the corresponding attribute can be verified
        """
        d = {'tests': 123}
        obj = Dynamic(**d)
        self.assertTrue(hasattr(obj, 'tests'))

    def test_03(self):
        """
        Test Case 03:
        Try instantiating a DynamicIterable object.
        
        Test is passed if the instance proves being a :py:class:`~xobox.utils.dynamic.DynamicIterable` instance.
        """
        obj = DynamicIterable()
        self.assertIsInstance(obj, DynamicIterable)

    def test_04(self):
        """
        Test Case 04:
        Insert data into a DynamicIterable object and verify dictionary-style accessibility.
        
        Test is passed if the added member is in the keys and the linked data equal to the inserted tests data.
        """
        obj = DynamicIterable()
        obj['tests'] = 123
        self.assertIn('tests', obj)
        self.assertEqual(obj['tests'], 123)

    def test_05(self):
        """
        Test Case 05:
        Insert data into a DynamicIterable object and verify object-style accessibility.
        
        Test is passed if the object proves having a corresponding attribute, providing the inserted tests data.
        """
        obj = DynamicIterable()
        obj['tests'] = 123
        self.assertTrue(hasattr(obj, 'tests'))
        self.assertEqual(obj.test, 123)

    def test_06(self):
        """
        Test Case 06:
        Create a DynamicIterable with initial data passed as dictionary.
        
        Test is passed if initial member is in the keys and the linked data is equal to the initial tests data.
        """
        d = {'tests': 123}
        obj = DynamicIterable(d)
        self.assertIn('tests', obj)
        self.assertEqual(obj['tests'], 123)

    def test_07(self):
        """
        Test Case 07:
        Create a DynamicIterable with initial data passed as keyword arguments.
        
        Test is passed if initial member is in the keys and the linked data is equal to the initial tests data.
        """
        d = {'tests': 123}
        obj = DynamicIterable(**d)
        self.assertIn('tests', obj)
        self.assertEqual(obj['tests'], 123)

    def test_08(self):
        """
        Test Case 08:
        Delete data from a DynamicIterable object after having added it.
        
        Test is passed if initially added attribute, key and data have disappeared.
        """
        d = {'tests': 123}
        obj = DynamicIterable(d)
        del obj['tests']
        self.assertNotIn('tests', obj)
        self.assertFalse(hasattr(obj, 'tests'))

    def test_09(self):
        """
        Test Case 09:
        Verify dictionary behaviour of DynamicIterable by initialising it with a dictionary.
        
        Test is passed if a dictionary comparison with the initialisation dictionary succeeds.
        """
        d = {'tests': 123}
        obj = DynamicIterable(d)
        self.assertTrue(d == obj)

    def test_10(self):
        """
        Test Case 10:
        Test pre-get and pre-set hooks by turning all keys to upper case.
        
        Test is passed if keys are upper case and get / set operations work without raising an exception.
        """
        def my_hook(key, value):
            return key.upper(), value

        obj = DynamicIterable()
        obj.register_hook('pre-set', my_hook)
        obj.register_hook('pre-get', my_hook)
        obj['foo'] = 'bar'
        try:
            result = obj['foo']
        except KeyError:
            result = False
        self.assertTrue(result)
        self.assertEqual(result, 'bar')
