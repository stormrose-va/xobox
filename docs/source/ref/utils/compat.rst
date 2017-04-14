Compatibility Utility
=====================

.. module:: xobox.utils.compat
   :synopsis: compatibility utility

.. py:currentmodule:: xobox.utils.compat

The :py:mod:`~xobox.utils.compat` module provides data, functions and classes whose interfaces have
changed with newer Python versions, or which are not available on all operating systems supported by
xobox. This allows using the most recent interface of these functions and classes within the xobox code,
without hacking around all along the code. Therefore, this module centralises all the dirty hacks which
become necessary when the Python standard library does not provide its own compatibility layer.


Constants
---------

.. autodata:: xobox.utils.compat.EX_OK

.. autodata:: xobox.utils.compat.EX_USAGE

.. autodata:: xobox.utils.compat.EX_DATAERR

.. autodata:: xobox.utils.compat.EX_NOINPUT

.. autodata:: xobox.utils.compat.EX_NOUSER

.. autodata:: xobox.utils.compat.EX_NOHOST

.. autodata:: xobox.utils.compat.EX_UNAVAILABLE

.. autodata:: xobox.utils.compat.EX_SOFTWARE

.. autodata:: xobox.utils.compat.EX_OSERR

.. autodata:: xobox.utils.compat.EX_OSFILE

.. autodata:: xobox.utils.compat.EX_CANTCREAT

.. autodata:: xobox.utils.compat.EX_IOERR

.. autodata:: xobox.utils.compat.EX_TEMPFAIL

.. autodata:: xobox.utils.compat.EX_PROTOCOL

.. autodata:: xobox.utils.compat.EX_NOPERM

.. autodata:: xobox.utils.compat.EX_CONFIG

.. autodata:: xobox.utils.compat.EX_NOTFOUND
