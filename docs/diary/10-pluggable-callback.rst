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
We'll also provide a default that can be overridden.

``directives.py``
=================

I'll start with a ``directives.py`` file in my extension directory. The
pattern will be:

- Change handlers are instances of a callable class

- The constructor takes the Pyramid config and presumably saves it

- The ``__call__`` is invoked on each change and is passed a list of
  tuples, a pair (the enum value for the kind of change and the string
  path to the file changed)

I put a minimum default handler that just does ``log.info``. The
``directives`` file also defines the directive to register a change
handler (doing nothing more than storing it in
`config.registry.settings['pyramid_watcher_handler']`).

``includeme``
===============

The plugin's ``includeme`` changed to:

- Make a default change handler instance and store it in the registry

- Add the directive

Sample App
==========

I changed the sample app to add a custom change handler in ``handlers.py``
and then registered it in ``main``.


