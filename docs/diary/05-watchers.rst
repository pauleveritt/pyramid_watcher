============
05: Watchers
============

Time to do some real coding. In this step I copy over code from Samuel
Colvin's ``watchgod``. Specifically, his
`watchers.py <https://github.com/samuelcolvin/watchgod/blob/master/watchgod/watcher.py>`_
and the test at
`test_watchers.py <https://github.com/samuelcolvin/watchgod/blob/master/tests/test_watch.py>`_.

watchgod_watcher.py
===================

I copied the file into ``src/pyramid_watcher/watchgod_watcher.py``. I
want it standalone so I can more easily keep it up-to-date with the
upstream. There will be come changes, though:

- I don't do the ``__all__`` dance

- The ``logger`` needs to be different

His license is also MIT, so I just need to give credit. I also used this
as the time to start my traditional ``TODO.md`` in the root, adding some
notes on things I'd like to come back to on that file, e.g. bringing back
some of the knobs like throttling that I left out.

It's important to get the tests in place early. I took the test file
and put it in ``tests/unit/test_watchgod_watcher.py``, removing the
parts that didn't apply (e.g. the watch function.)

His tests have a nice convenience function dependency on
``pytest_toolbox`` so I added that to the test dependencies.