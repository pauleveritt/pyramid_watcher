============
12: Refactor
============

I have some stuff in place. The code has grown somewhat organically but
is a bit messy. Let's take a moment to do some refactoring.

``models.py``
=============

I use type annotations which means I import classes. This has led to circular
references. I will try putting some of these dataclasses into a ``models.py``
file. It's a common pattern in Pyramid.

Manual, Explicit Configuration
==============================

I'm using decorators plus sub-``includeme`` functions to get the wiring
close to the code being wired. But it also makes it hard to get a
birds-eye view of what ``pyramid_watcher`` does. Especially, it is harder
for Michael to do a review.

I am moving this to a model where all configuration is done in
``pyramid_watcher/__init__.py`` with copious comments. No more decorators,
no more ``config.scan()``. with this you can see the whole picture just by
reading that file's ``includeme()``.

Docstrings and Comments
=======================

Added extensive docstrings (and comments) to help understanding.

Frozen Dataclasses
==================

Premature optimization but it actually fits. These changeset instances are
like a log and should never change.


