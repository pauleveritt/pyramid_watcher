=================
04: Hello Testing
=================

I'd like to do TDD from the beginning on this project. Frankly, I have
the time to go at a measured pace and TDD helps me feel in control.

Let's get the machinery in place for testing, all working well in PyCharm:

- pytest and ``pytest.ini``

- coverage and ``.coveragerc``

- Travis setup to run tests on pushes

.. note::

    Let's save tox for later.

pytest
======

We already have ``pytest`` installed from :doc:`01-packaging` but
just in case...run ``pip install -e .[testing]`` to get the correct
dependencies.

Add a ``pytest.ini`` file at the root with:

.. code-block:: ini

    [pytest]
    testpaths = tests
    python_files = test*.py

I don't think either of those are needed, but I'm following Michael's
``setup.cfg`` section.

Just to have something to test, I created ``tests/unit/test_includeme.py``
which later will test Pyramid's ``includeme`` configuration suppport.
I added an ``includeme`` function in ``__init__.py`` that returns a
flag for now.

For PyCharm, I had to go to the settings for Python Integrated Tools and
make pytest the default test runner.

The test passed. Yay.

Coverage
========

It's important to get coverage to exclude your virtual environment, docs
area, and tests. You want it to run fast. So make a ``.coveragerc`` in the
root with:

.. code-block:: ini

    [run]
    source = pyramid_watcher
    omit =
        */.venv/*
        */docs/*
        */tests/*
        */.pytest_cache/*

If we put this in ``pytest.ini``, PyCharm won't pick it up. This aspect
is always a little fiddly and irritating.

Travis
======

Travis is the dominant CI in open source. I created a basic ``.travis.yml``
in the root:

.. code-block:: yaml

    language: python
    python:
      - '3.5'
    cache: pip
    install:
      - pip install -e .[testing]
    script:
      - py.test --cov-report term-missing --cov app -v

.. note::

    I'll add in 3.6 and 3.7 later, once I get Travis setup well.

I logged into Travis, clicked the ``+``, and linked Travis to this repo.
I then committed and pushed. Travis built on all 3 interpreters.

After a couple of failures, it appeared the ``testpaths = pyramid_watcher``
line in my ``pytest.ini`` was causing tests to fail. I replaced that line
with ``norecursedirs = .git docs _build tmp* .venv`` which I had used on
previous projects. Not the same thing, so I'll have to get back to this
later.