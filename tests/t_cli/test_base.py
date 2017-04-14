# -*- coding: utf-8 -*-

"""
    tests.t_cli.test_base
    ~~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


from unittest import TestCase
from xobox.cli.base import BaseCommand


class TestXoboxCliBase(TestCase):
    """
    Unit tests for :py:mod:`xobox.cli.base`
    """

    def test_01(self):
        """
        Test Case 01:
        Try creating an instance of :py:class:`~xobox.cli.base.BaseCommand`.
        
        Test is passed if instance is an instance of :py:class:`~xobox.cli.base.BaseCommand`.
        """
        obj = BaseCommand()
        self.assertIsInstance(obj, BaseCommand)

    def test_02(self):
        """
        Test Case 02:
        Try calling :py:meth:`~xobox.cli.base.BaseCommand.handle` method.
        
        Test is passed if :py:exc:`NotImplementedError` is raised.
        """
        obj = BaseCommand()
        with self.assertRaises(NotImplementedError):
            obj.handle()
