xobox' Application Configuration
================================

.. module:: xobox.conf
   :synopsis: xobox' application configuration module

xobox' application configuration module provides an interface for accessing
built-in default configuration constants. Instead of scattering default constants
all over the application's code, default values shall be centralized in
:py:mod:`xobox.conf.default`. This being the case, these configuration defaults
can be accessed by either the function interface, or by a class interface.

Function Interface
------------------

.. py:currentmodule:: xobox.conf

.. autofunction:: xobox.conf.get_conf


Class Interface
---------------

.. py:currentmodule:: xobox.conf

.. class:: xobox.conf.ApplicationConf

   .. method:: get_instance(*args, **kwargs)

      Obtain the reference to the instance of :py:class:`~xobox.conf.ApplicationConf`. If no
      instance exists yet, one will be created and its reference returned.

      .. note::

         Although the :py:meth:`~xobox.conf.ApplicationConf.get_instance` method accepts arbitrary
         positional and keyword arguments, they will be ignored by the constructor.


Default Configuration Values
----------------------------

.. module:: xobox.conf.default
   :synopsis: xobox' default configuration values

.. py:currentmodule:: xobox.conf.default


Core Settings
~~~~~~~~~~~~~

.. autodata:: xobox.conf.default.DEFAULT_CHARSET

.. autodata:: xobox.conf.default.DEFAULT_PICKLE_PROTOCOL

.. autodata:: xobox.conf.default.DEFAULT_XOBOX_EXECUTABLE


Logging Settings
~~~~~~~~~~~~~~~~

.. autodata:: xobox.conf.default.DEFAULT_LOG_TYPE

.. autodata:: xobox.conf.default.DEFAULT_LOG_LEVEL

.. autodata:: xobox.conf.default.DEFAULT_LOG_FILE

.. autodata:: xobox.conf.default.DEFAULT_LOG_TIMESTAMP

.. autodata:: xobox.conf.default.DEFAULT_LOG_COLOR
