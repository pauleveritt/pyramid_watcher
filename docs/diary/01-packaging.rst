=============
01: Packaging
=============

This is a place where I frequently get wrapped around the axle. I want
to adhere to "latest and greatest" but there's (a) so much to think about
and (b) little consistency. I wasted a lot of time looking at PyScaffold,
pbr, and various cookiecutters before deciding "screw it, get on with it"
and following Michael's pattern.

Background
==========

setup.py
--------

It's a package so you need a `setup.py`. Oh, wait, with modern pip and
``pyproject.toml`` you can forget that? After a bunch of research, I
decided it was too soon on that.

I copied the ``setup.py`` from Michael's ``hupper``, changed ``hupper``
to ``pyramid_watcher``, then did some other things:

- I made some other "requires" blocks, e.g. for the sample app I plan
  to write

- I pinned this to Python 3.5+ due to ``scandir``

- I kept his entry point for a console script. That will be needed much
  later on, but it's easy to forget to re-run ``pip install -e .`` to
  get the console scripts generated

Michael's layout follows Hyneks's recommendation to put sources under
``src/<packgage_name>``.

setup.cfg
---------

I removed his section about pyflake, as I'm a PyCharm guy. (Plus I plan
to add ``black`` late.) I removed the ``pytest`` section...I'll put
that into a ``pytest.ini`` so that PyCharm will pick it up. I should
research if PyCharm will get those settings from ``setup.cfg``.

Other
-----

I started a ``README.rst`` and ``CHANGES.txt``. I made an empty
``src/pycharm_watcher/__init__.py`` and made
``src/pycharm_watcher/cli.py`` with an empty ``main``.