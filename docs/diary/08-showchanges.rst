================
08: Show Changes
================

In this step I'll wire up the "Echo" sample app to actually show
information about a batch of changes. This will start to involve
some Pyramid machinery, primarily in the ``includeme`` of the
plugin.

``includeme``
=============

The bulk of the changes are in the ``__init__.py`` of the
``pyramid_watcher`` package. The ``includeme`` is where we wire things
into Pyramid. Here I made an instance  of ``ThreadRunner`` using a
very simple callback (log to the console) and directory to watch
(the current working directory).

That turned out to be dumb. Pyramid's reloader (which uses hupper)
stepped in and restarted the process. I changed it to point to the
``docs`` directory, naively done with ``../../../../docs``.

Now a modification to a file in the docs directory cases something
like this to be sent to the console::

  (<FileChangeInfo.modified: 2>, '../../../../docs/diary/08-showchanges.rst')

