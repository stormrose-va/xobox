# -*- coding: utf-8 -*-

"""
    xobox.utils.compat
    ~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by the Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""

try:
    from os import EX_OK
except ImportError:
    #: Exit code that means no error occurred.
    EX_OK = 0

try:
    from os import EX_USAGE
except ImportError:
    #: Exit code that means the command was used incorrectly, such as when the wrong number of arguments are given.
    EX_USAGE = 1

try:
    from os import EX_DATAERR
except ImportError:
    #: Exit code that means the input data was incorrect.
    EX_DATAERR = 2

try:
    from os import EX_NOINPUT
except ImportError:
    #: Exit code that means an input file did not exist or was not readable.
    EX_NOINPUT = 3

try:
    from os import EX_NOUSER
except ImportError:
    #: Exit code that means a specified user did not exist.
    EX_NOUSER = 4

try:
    from os import EX_NOHOST
except ImportError:
    #: Exit code that means a specified host did not exist.
    EX_NOHOST = 5

try:
    from os import EX_UNAVAILABLE
except ImportError:
    #: Exit code that means that a required service is unavailable.
    EX_UNAVAILABLE = 6

try:
    from os import EX_SOFTWARE
except ImportError:
    #: Exit code that means an internal software error was detected.
    EX_SOFTWARE = 7

try:
    from os import EX_OSERR
except ImportError:
    #: Exit code that means an operating system error was detected, such as the inability to fork or create a pipe.
    EX_OSERR = 8

try:
    from os import EX_OSFILE
except ImportError:
    #: Exit code that means some system file did not exist, could not be opened, or had some other kind of error.
    EX_OSFILE = 9

try:
    from os import EX_CANTCREAT
except ImportError:
    #: Exit code that means a user specified output file could not be created.
    EX_CANTCREAT = 10

try:
    from os import EX_IOERR
except ImportError:
    #: Exit code that means that an error occurred while doing I/O on some file.
    EX_IOERR = 11

try:
    from os import EX_TEMPFAIL
except ImportError:
    #: Exit code that means a temporary failure occurred. This indicates something that may not really be an error,
    #: such as a network connection that couldn't be made during a retryable operation.
    EX_TEMPFAIL = 12

try:
    from os import EX_PROTOCOL
except ImportError:
    #: Exit code that means that a protocol exchange was illegal, invalid, or not understood.
    EX_PROTOCOL = 13

try:
    from os import EX_NOPERM
except ImportError:
    #: Exit code that means that there were insufficient permissions to perform the operation (but not intended
    #: for file system problems).
    EX_NOPERM = 14

try:
    from os import EX_CONFIG
except ImportError:
    #: Exit code that means that some kind of configuration error occurred.
    EX_CONFIG = 15

try:
    from os import EX_NOTFOUND
except ImportError:
    #: Exit code that means something like "an entry was not found".
    EX_NOTFOUND = 16
