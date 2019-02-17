======================
10: Pluggable Callback
======================

We'd like to "do something" with the change information. Currently I just
log it to info. We'd like a smarter callback, and in fact, make it possible
for an application to override the default callback.

Gameplan
========

We'd like one and only one callback to process the changes. We'd like to
it replaceable, but still, there should only be one.

That means Pyramid events aren't a good choice for this handler. Although
events might be something the handler itself uses, to let interested
code know that an image was added.

We'll use a directive that stores a callable in the registry's settings.
We'll also provide a default.

``directives.py``
=================

I'll start with a ``directives.py`` file in my extension directory.
The minimum is easy:

