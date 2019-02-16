==========
02: Sphinx
==========

Rather than run ``sphinx-build``, I copied the ``conf.py`` from
```hupper`` and trimmed out all the latex etc. unused stuff. It wired up
the Pyramid theme.

I then added these pages about the diary and setup a PyCharm run
configuration. I don't use the Sphinx run configuration type as I
sometimes want to run under the debugger. Instead I make a Python run
configuration with:

- ``Module name:`` set to ``sphinx.cmd.build``
- ``Parameters:`` set to ``-b html . _build``
- ``Working directory`` set to the ``docs`` directory

To view the output, rather than setup a local HTTP server, I use
PyCharm:

- Select ``docs/_build/index.html``
- Right-click
- Choose ``Run 'index.html'``

PyCharm runs a local HTTP server and launches a browser.

Finally, I started writing entries in ``CHANGES.txt``. Hopefully I'll
get back to using ``gitchangelog`` to generate that automatically.
