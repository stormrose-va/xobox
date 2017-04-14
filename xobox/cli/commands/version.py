# -*- coding: utf-8 -*-

"""
    xobox.cli.commands.version
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""


import xobox
from ..base import BaseCommand


class VersionCommand(BaseCommand):
    """
    Command class implementing the version command.
    """

    name = 'version'
    aliases = ('--version', '-v')
    help = 'Show version and copyright information'
    arguments = (
        (('-s', '--short'), {'help': 'only print the version string', 'action': 'store_true'}),
    )

    def handle(self):
        """Command handler for the version command"""
        if 'short' in self.args and self.args.short:
            self.log_notice(xobox.get_version())
        else:
            self.log_notice("""xobox version {version}
Copyright (C) {year} {author}
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. """.format(
                version=xobox.get_version(),
                year=xobox.COPYRIGHT[0],
                author=xobox.COPYRIGHT[1])
            )
        self._status = 0
