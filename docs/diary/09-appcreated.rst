========================
ApplicationCreated Event
========================

My tests are hanging. Clearly related to including my ``pyramid_watcher``
plugin during startup. What to do?

Michael gave a review of the code and suggested deferring startup of
the watcher as long as possible by using Pyramid's
`ApplicationCreated event <https://docs.pylonsproject.org/projects/pyramid/en/latest/api/events.html>`_.
Meaning, write a subscriber to watch for this event to fire, which doesn't
happen until ``config.make_wsgi_app()`` is fired.

In this step I'll wire up that event and then get the tests back in shape.

``src/pyramid_watcher/subscribers.py``
======================================

It's common for Pyramid extensions to subscribe to events and thus to put
these subscribers prominently in a ``subscribers.py`` file.

I'll actually start with ``tests/unit/test_subscribers.py`` to make sure
I'm doing at least a bit of TDD.

I'm using type hinting on the subscriber, saying that the ``event`` passed
in is an instance of ``ApplicationCreated``.

I took all of the code in ``includeme`` and moved it to the subscriber,
leaving behind a ``config.scan('.subscriber')`` to process the
decorator. I could have done this imperatively, instead of scanning, but
I find the decorator approach easier to read.

By moving this all to the subscriber, I defer all the work of the
ThreadRunner -- not just the starting, but the creation -- as late as
possible. This opens the opportunity to let the application add to the
list of paths to watch as part of startup, rather than only coming from
the config file.

All well and good, but it still didn't stop the problem with the
application hanging.