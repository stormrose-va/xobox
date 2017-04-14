xobox' Command Line Interface
=============================

.. module:: xobox.cli
   :synopsis: xobox' command line interface

xobox' command line interface is contained within the :py:mod:`xobox.cli` package. It offers only one function at
package level which can be called directly. This function is usually called from a Python script acting as executable
interface.

.. py:currentmodule:: xobox.cli

.. autofunction:: xobox.cli.execute

   The :py:func:`~xobox.cli.execute` function will create a :py:class:`~xobox.cli.dispatch.CommandDispatcher`
   instance, which provides the logic for invoking a command.


Dispatcher
----------

.. module:: xobox.cli.dispatch
   :synopsis: xobox's command line dispatcher

.. py:currentmodule:: xobox.cli.dispatch

.. autoclass:: xobox.cli.dispatch.CommandDispatcher
   :members:


Command Line Commands
---------------------

Command line commands are implemented as modules within the :py:mod:`xobox.cli.commands` package.
The module name itself must be unique within the :py:mod:`~xobox.cli.commands` package, but has no
direct link to the command's external designator used on the command line.

.. module:: xobox.cli.base
   :synopsis: base for command line commands to inherit from

All command line commands are implemented as classes, inheriting from :py:class:`xobox.cli.base.BaseCommand`:

.. py:currentmodule:: xobox.cli.base

.. autoclass:: xobox.cli.base.BaseCommand
   :members:


Writing a Command Line Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writing a command line command can be as easy as creating a Python module within the
:py:mod:`xobox.cli.commands` package containing a class inheriting from
:py:class:`~xobox.cli.base.BaseCommand` and overriding some basic settings:

.. code-block:: python

   from xobox.cli.base import BaseCommand

   class MyCommand(BaseCommand)
      name = 'foo'
      aliases = ('bar', 'baz')
      help = 'The super foo command that makes you bar'

Looks easy? It actually is, since :py:class:`~xobox.cli.dispatch.CommandDispatcher`
is performing all the black magic needed to detect available commands, make up decent usage
messages out of the information provided by each command's implementation, parsing eventual
command line arguments required by the different commands and finally setting up the environment
and running the command.

Unfortunately, this command would not be of any use -- once invoked by the dispatcher, it will
simply raise a :py:exc:`NotImplementedError` exception. This is simply for the fact that each
command needs to implement its own :py:meth:`~xobox.cli.base.BaseCommand.handle` method.
Since this has not happened here, the :py:meth:`~xobox.cli.base.BaseCommand.handle` method
inherited from the :py:class:`~xobox.cli.dispatch.CommandDispatcher` class will be used, and
this one simply raises a :py:exc:`NotImplementedError` exception.

When implementing your own :py:meth:`~xobox.cli.base.BaseCommand.handle` method, please
take care of the following conventions.

User Interaction
^^^^^^^^^^^^^^^^

Whenever possible, user interaction shall be avoided. The concept of xobox is to gather all
required information either form command line arguments or from configuration files, and then to
run silently, only outputting status information according to the log level set by the user.

This restriction has been set in order to respecting that one important use case is to run
xobox as batch job, where no user interaction is possible.

Output
^^^^^^

All output to the user interface shall be channelled through the appropriate ``log_...()`` methods
each command class has inherited from the :py:class:`~xobox.cli.base.BaseCommand` class.
This ensures the output is only sent if the user has selected the corresponding log level, and it
is sent through the right channel.

.. warning::

   **Never** use Python's :py:func:`print` function to generate and send output to the user
   interface. This will break xobox's promise of being 100% batch job enabled, including
   logging its output to a file.

Status
^^^^^^

xobox uses the :py:attr:`~xobox.cli.base.BaseCommand.status` property any command
has inherited from the :py:class:`~xobox.cli.base.BaseCommand` class for setting an
appropriate exit status when terminating xobox's main process.

By default, a command object's status is set to :py:data:`os.EX_OK`. If necessary or appropriate, the
status information can be changed within the :py:meth:`~xobox.cli.base.BaseCommand.handle` method
by overwriting the internal ``_status`` member::

   def handle(self):
      self._status = xobox.utils.compat.EX_USAGE


Existing Command Line Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. module:: xobox.cli.commands
   :synopsis: package containing all command line commands

Version Command
^^^^^^^^^^^^^^^

.. module:: xobox.cli.commands.version
   :synopsis: module implementing the version command

.. py:currentmodule:: xobox.cli.commands.version

.. autoclass:: xobox.cli.commands.version.VersionCommand
   :members:
   :undoc-members:

Logging Interface
-----------------

.. module:: xobox.cli.logger
   :synopsis: xobox' output interface

The :py:mod:`~xobox.cli.logger` module is responsible for handling any
output that shall be transported to the user. It implements the magic behind
the ``log_...()`` methods provided by the :py:class:`~xobox.cli.dispatch.CommandDispatcher`
class, allowing command implementations to easily transporting information to the user interface.

The :py:mod:`~xobox.cli.logger` module provides a class interface,
offering a flexible message output system:

.. py:currentmodule:: xobox.cli.logger

.. class:: xobox.cli.logger.Logger

   .. method:: get_instance(*args, **kwargs)

      Obtain the reference to the instance of :py:class:`~xobox.cli.logger.Logger`. If no
      instance exists yet, one will be created and its reference returned.

      .. warning::

         If a logger instance already exists (e. g. due to an earlier invocation from another
         module or function), any passed keyword arguments will be ignored. Therefore, it is
         safer to not using any keyword arguments, but setting the logger's properties appropriately
         after having received the logger instance's reference.

   .. method:: log(level, message)

      Register a log message within the logging queue and flush the queue afterwards (currently
      log messages are not cached).

      :param str level:   The log level to be used for the message to be passed. Must be one of
                          *error*, *warning*, *notice*, *info*, *debug* or *usage*.
      :param str message: The message string to be recorded

   .. method:: log_error(message)

      Convenience shortcut for registering messages with log level `error`

      :param str message: The message string to be recorded

   .. method:: log_warning(message)

      Convenience shortcut for registering messages with log level `warning`

      :param str message: The message string to be recorded

   .. method:: log_notice(message)

      Convenience shortcut for registering messages with log level `notice`

      :param str message: The message string to be recorded

   .. method:: log_info(message)

      Convenience shortcut for registering messages with log level `info`

      :param str message: The message string to be recorded

   .. method:: log_debug(message)

      Convenience shortcut for registering messages with log level `debug`

      :param str message: The message string to be recorded

   .. method:: log_usage(message)

      Convenience shortcut for registering messages with log level `usage`

      :param str message: The message string to be recorded

   .. attribute:: color

      Boolean switch indicating whether this logger allows colored output.

   .. attribute:: file

      The log file used when run as file logger. Must be a string indicating the
      path name of the file to log into.

   .. attribute:: level

      The log level (string). Expected to be one of `mute`, `error`, `warning`, `info` or `debug`.

   .. attribute:: type

      The logger type (string). Expected to be one of `term` or `file`.
