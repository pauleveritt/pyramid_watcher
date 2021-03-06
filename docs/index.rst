===============
pyramid_watcher
===============

Want to watch your local files and take actions, including reloading a
browser, when add/edit/change modifications are detected?
pyramid_watcher works in a background thread and lets you register
handlers.

This package is written specifically as a start to a static-site
generator which watches Markdown files.

Scanning
========

This package uses Python's builtin
`scandir <https://docs.python.org/3/library/os.html#os.scandir>`_
module from `PEP 471 <https://www.python.org/dev/peps/pep-0471/>`_
and thus requires Python 3.5 or higher. As noted by Samuel Colvin in
the README for `watchgod <https://pypi.org/project/watchgod/>`_, this
approach is plenty fast and mitigates the need to use OS-native
filesystem watching.

Acknowledgements
================

The world of JavaScript has tons of tools like webpack-dev-server which
watch for changes and go through rich pipelines to then do interesting
reload operations in the browser.

Hsiaoming Yang (lepture) manages a `livereload <https://pypi.org/project/livereload/>`_
package which does much of this. I wanted a few differences: integration
with Pyramid in a rich way, higher-performance watching, and batch
operations.

Samuel Colvin's `watchgod <https://pypi.org/project/watchgod/>`_ was the
architectural inspiration. The ``scandir`` approach and code was taken
directly from his ``watchers.py`` file. His package does more things and
is dependent on asyncio stuff.

Michael Merickel's `hupper <https://pypi.org/project/hupper/>`_ gave me
the background thread approach registered with Pyramid. Far more
importantly, Michael coached me through the entirety of writing this.

Installation
============

Stable release
--------------

To install pyramid_watcher, run this command in your terminal:

.. code-block:: console

    $ pip install pyramid_watcher

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/

More Information
================

.. toctree::
   :maxdepth: 1

   diary/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`