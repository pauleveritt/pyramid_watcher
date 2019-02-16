================
06: ThreadRunner
================

With the code in place for watching files, I need a thread runner that
can work with Pyramid. With this, watching happens in the background
and a callable is executed with each batch of changes reported by the
``watchgod`` code.

Remember, I want to keep Pyramid stuff out of the watchgod side.

threadrunner.py
===============

I made a file ``src/pyramid_watcher/threadrunner.py`` and put into it
code that Michael adapted from
`hupper.polling.PollingFileMonitor <https://github.com/Pylons/hupper/blob/master/src/hupper/polling.py>`_.

I did a few changes: I added some type hinting and started the use of
Python ``pathlib`` usage. (Need to add that on the watchgod side, made
a TODO.)

The tests in ``hupper`` don't have anything that covers it, and I'm not
that smart, so I'll come back to it.

Nope, changed my mind. Decided to at least write a test that imports it
and constructs an instance.