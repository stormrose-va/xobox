# -*- coding: utf-8 -*-

"""
    tests.t_cli.test_logger
    ~~~~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


import os
import sys
import tempfile
from unittest import TestCase, skipIf
from xobox.cli.logger import Logger


class TestXoboxCliLogger(TestCase):
    """
    Unit tests for :py:mod:`xobox.cli.logger`
    """

    @skipIf(sys.version_info < (3, 0, 0), "Singleton instance recognition only works in Python 3")
    def test_01(self):
        """
        Test Case 01:
        Try getting an instance of :py:class:`~xobox.cli.logger.Logger`.
        
        Test is passed if instance is an instance of :py:class:`~xobox.cli.logger.Logger`.
        """
        obj = Logger.get_instance()
        self.assertIsInstance(obj, Logger)

    def test_02(self):
        """
        Test Case 02:
        Test logger by logging a tests message into a file.
        
        Test is passed if file content meets expectation.
        """
        fd, name = tempfile.mkstemp()
        os.close(fd)
        logger = Logger.get_instance()
        logger.file = name
        logger.type = 'file'
        logger.log_error("This is a tests message")
        logger.type = 'term'
        fp = open(name, 'r')
        content = fp.read()
        fp.close()
        os.unlink(name)
        self.assertRegexpMatches(
            content,
            r'^\[\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}\] \[ERROR\] This is a tests message$'
        )
