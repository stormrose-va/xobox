# -*- coding: utf-8 -*-

"""
    tests.t_cli.t_commands.test_version
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


from unittest import TestCase
from xobox.cli.base import BaseCommand
from xobox.cli.commands.version import VersionCommand


class TestXoboxCliCommandsVersion(TestCase):
    """
    Unit tests for :py:mod:`xobox.cli.commands.version`
    """

    def test_01(self):
        """
        Test Case 01:
        Check if :py:class:`~xobox.cli.commands.version.VersionCommand` is a subclass of
        :py:class:`~xobox.cli.commands.base.BaseCommand`.
        
        Test is passed if :py:class:`~xobox.cli.commands.version.VersionCommand` is a subclass of
        :py:class:`~xobox.cli.commands.base.BaseCommand`.
        """
        self.assertTrue(issubclass(VersionCommand, BaseCommand))

    def test_02(self):
        """
        Test Case 02:
        Try creating an instance of :py:class:`~xobox.cli.commands.version.VersionCommand`.
        
        Test is passed if instance proves being an instance of
        :py:class:`~xobox.cli.commands.version.VersionCommand`.
        """
        obj = VersionCommand()
        self.assertIsInstance(obj, VersionCommand)
