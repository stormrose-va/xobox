# -*- coding: utf-8 -*-

"""
    tests.test_xobox
    ~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


from unittest import TestCase, skipUnless
import xobox


class TestXobox(TestCase):
    """
        Unit tests for :py:mod:`xobox`
        """

    def test_01(self):
        """
        Test Case 01:
        Test type of :py:data:`xobox.VERSION`
        
        Test is passed if type of :py:data:`xobox.VERSION` is a tuple
        """
        self.assertIsInstance(xobox.VERSION, tuple)

    def test_02(self):
        """
        Test Case 02:
        Test length of :py:data:`xobox.VERSION`
        
        Test is passed if detected length is 5
        """
        self.assertEqual(len(xobox.VERSION), 5)

    def test_03(self):
        """
        Test Case 03:
        Test type of first member of :py:data:`xobox.VERSION`
        
        Test is passed if detected type is :py:class:`int` and value is not negative
        """
        self.assertIsInstance(xobox.VERSION[0], int)
        self.assertGreaterEqual(xobox.VERSION[0], 0)

    def test_04(self):
        """
        Test Case 04:
        Test type of second member of :py:data:`xobox.VERSION`
        
        Test is passed if detected type is :py:class:`int` and value is not negative
        """
        self.assertIsInstance(xobox.VERSION[1], int)
        self.assertGreaterEqual(xobox.VERSION[1], 0)

    def test_05(self):
        """
        Test Case 05:
        Test type of third member of :py:data:`xobox.VERSION`
        
        Test is passed if detected type is :py:class:`int` and value is not negative
        """
        self.assertIsInstance(xobox.VERSION[2], int)
        self.assertGreaterEqual(xobox.VERSION[2], 0)

    def test_06(self):
        """
        Test Case 06:
        Test type of fifth member of :py:data:`xobox.VERSION`
        
        Test is passed if detected type is :py:class:`int` and value is not negative
        """
        self.assertIsInstance(xobox.VERSION[4], int)
        self.assertGreaterEqual(xobox.VERSION[4], 0)

    def test_07(self):
        """
        Test Case 07:
        Test type of fourth member of :py:data:`xobox.VERSION`
        
        Test is passed if member is one of ``alpha``, ``beta``, ``rc``, ``final``
        """
        allowed = ('alpha', 'beta', 'rc', 'final')
        self.assertIn(xobox.VERSION[3], allowed)

    @skipUnless(xobox.VERSION[3] == 'final', 'Test is only for final releases')
    def test_08(self):
        """
        Test Case 08:
        Test suffix plausibility for final releases
        
        Test is passed if suffix is zero.
        """
        self.assertEqual(xobox.VERSION[4], 0)

    @skipUnless(xobox.VERSION[3] in ('beta', 'rc'), 'Test is only for pre-releases')
    def test_09(self):
        """
        Test Case 09:
        Test suffix plausibility for pre-releases
        
        Test is passed if suffix is greater than zero.
        """
        self.assertGreater(xobox.VERSION[4], 0)

    def test_10(self):
        """
        Test Case 10:
        Test type of :py:data:`xobox.COPYRIGHT`
        
        Test is passed if type of :py:data:`xobox.COPYRIGHT` is a tuple
        """
        self.assertIsInstance(xobox.COPYRIGHT, tuple)

    def test_11(self):
        """
        Test Case 11:
        Test length of :py:data:`xobox.COPYRIGHT`
        
        Test is passed if detected length is 2
        """
        self.assertEqual(len(xobox.COPYRIGHT), 2)

    def test_12(self):
        """
        Test Case 12:
        Test type of first member of :py:data:`xobox.COPYRIGHT`
        
        Test is passed if detected type is :py:class:`str`
        """
        self.assertIsInstance(xobox.COPYRIGHT[0], str)

    def test_13(self):
        """
        Test Case 13:
        Test type of second member of :py:data:`xobox.COPYRIGHT`
        
        Test is passed if detected type is :py:class:`str`
        """
        self.assertIsInstance(xobox.COPYRIGHT[1], str)

    def test_14(self):
        """
        Test Case 14:
        Test type of :py:data:`xobox.APPINFO`
        
        Test is passed if type of :py:data:`xobox.APPINFO` is a tuple
        """
        self.assertIsInstance(xobox.APPINFO, tuple)

    def test_15(self):
        """
        Test Case 15:
        Test length of :py:data:`xobox.APPINFO`
        
        Test is passed if detected length is 2
        """
        self.assertEqual(len(xobox.APPINFO), 2)

    def test_16(self):
        """
        Test Case 16:
        Test type of first member of :py:data:`xobox.APPINFO`
        
        Test is passed if detected type is :py:class:`str`
        """
        self.assertIsInstance(xobox.APPINFO[0], str)

    def test_17(self):
        """
        Test Case 17:
        Test type of second member of :py:data:`xobox.APPINFO`

        Test is passed if detected type is :py:class:`str`
        """
        self.assertIsInstance(xobox.APPINFO[1], str)

    def test_18(self):
        """
        Test Case 18:
        Test :py:func:`xobox.get_app_name`
        
        Test is passed if return value equals to second member of :py:data:`xobox.APPINFO` 
        """
        self.assertEqual(xobox.get_app_name(), xobox.APPINFO[1])

    def test_19(self):
        """
        Test Case 19:
        Test :py:func:`xobox.get_app_author`

        Test is passed if return value equals to first member of :py:data:`xobox.APPINFO` 
        """
        self.assertEqual(xobox.get_app_author(), xobox.APPINFO[0])
