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

When I first did this, RTD failed to build, saying it didn't have the
pylons theme. I forgot about this: installs that need to build the docs
have to run ``pip install -e .[docs]`` to get the ``extras_requires``.
I added ``extra_requirements: docs`` to ``.readthedocs.yml`` and pushed.

Other Work
==========

I realized that I don't want a CLI entry point in ``setup.py`` as I'll be
using Pyramid's command-line pluggability. I removed the ``entry_points``
from ``setup.py`` and deleted ``cli.py``. To make sure there are no
fossils, I re-ran ``pip install -e .``.

After this step I'm switching to doing each of these units on a branch.

Since I now have a
`docs page <>`_, I edited the GitHub repo's description to include a link to
the docs, as well as mentioning it in ``README.rst``. Hell, I even added a
badge to the README for the RTD status.