===================
07: Echo Sample App
===================

Time to make a sample Pyramid app that can then put to work some Pyramid
integration. This app is simply going to echo the batch of changes
coming from a callback.

.. note::

    Remember to run ``pip install -e .[sample]`` to get the dependencies
    needed (``pyramid_jinja2``, ``waitress``, etc.)

``samples/echo/__init__.py``
============================

Make a small WSGI app which does the normal Pyramid setup, plus a
few other things:

- Import a root resource and use it to bootstrap the configurator's
  root factory. This isn't strictly necessary but helps pave the way
  for future stuff.

- ``config.scan`` for views

- ``config.scan`` the (soon to be written) ``includeme`` in our
  extension

``resources.py``
================

Make a class for the root resource then a bootstrap function that
makes an instance to return to the Configurator's root factory.

``samples/echo/development.ini``
================================

Did a little trick to allow multiple samples to be usable from config
files. I changed ``setup.py`` to have entry points named for each
sample WSGI application, then referred to them here.

For example, in ``setup.py``:

.. code-block:: python

    'echo = pyramid_watcher.samples.echo:main',

...and in ``development.ini``:

.. code-block:: ini

    [app:main]
    use = egg:pyramid_watcher#echo

``views.py``
============

I made a simple view for a root resource.

``templates/siteroot_view.jinja2``
==================================

I had to make a ``templates`` folder in ``echo``. In PyCharm, I marked it
as a ``Templates`` folder, which prompted me to set a template language
for the project.

I added ``siteroot_view.jinja2`` which was used for the default view
of the ``SiteRoot`` context. It uses a default template so I added that
too.

Tests
=====

These are sample applications so we don't really want to unit test them.
But we can do functional tests. It's a nice way to develop, especially
when doing TDD mode in PyCharm.

I made a directory ``tests/functional`` with a ``conftest.py`` in it.
I then made a directory ``sample/echo`` with a ``conftest.py`` in there
as well as the first test.

It seems I forgot the ``WebTest`` testing_requires dependency in
``setup.py`` so I added it and re-ran install.