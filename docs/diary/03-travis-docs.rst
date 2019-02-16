===============
03: ReadTheDocs
===============

We want to share our docs and `ReadTheDocs <https://readthedocs.org>`_
is a wonderful resource. You log into your RTD account and connect it to
a GitHub repo. With each push, it rebuilds docs.

We'll follow the guide for using a
`configuration file <https://docs.readthedocs.io/en/latest/config-file/index.html>`_
in the
`V2 <https://docs.readthedocs.io/en/latest/config-file/v2.html>`_ format.
This means a ``.readthedocs.yml`` file in the project root.

It's very simple. Nothing big to report.

Other Work
==========

I realized that I don't want a CLI entry point in ``setup.py`` as I'll be
using Pyramid's command-line pluggability. I removed the ``entry_points``
from ``setup.py`` and deleted ``cli.py``. To make sure there are no
fossils, I re-ran ``pip install -e .``.

After this step I'm switching to doing each of these units on a branch.