Termcolor Utility
=================

.. module:: xobox.utils.termcolor
   :synopsis: termcolor utility

.. py:currentmodule:: xobox.utils.termcolor

The termcolor utility provides means to detect whether a system environment technically supports
coloured output on a terminal (:py:data:`sys.stdout`) or not. It relies on information provided
by the file object itself and :py:data:`sys.platform`.

.. autofunction:: xobox.utils.termcolor.supports_color
