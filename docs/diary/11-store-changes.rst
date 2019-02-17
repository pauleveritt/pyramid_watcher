=================
11: Store Changes
=================

I have a sample app called "Echo" which...isn't echoing. Meaning, we want
the browser to show the change events.

I need to store the events somewhere. Later the events will update items in
a tree of resources. For this simple demo, I just want to update the
site root resource, appending change events as they come in.

Thus, I'll have my sample app's custom change handler:

- Grab the site root

- Pass the batch of changes to a method on the site root

The site root will just append the changes to list and I'll change the
template to format that data on the resource.

Semi-Persistent Resources
=========================

First, a snag. Our instance of ``echo.resources.SiteRoot`` is created and
thrown away on every request. We could make an instance at the module
level of ``resources`` but that makes testing hard.

As a temporary solution, I made a site root instance in the ``includeme``
and stored it in the registry. It's likely not very cool to store
arbitrary data in the registry. But this is an example app.

``echo/resources.py``
=====================

The root factory was then changed to just get the value from the registry.

With that in place, I added a dataclass field for storing the changes and
a method ``handle_changes`` that would be passed the change set.

``echo/handlers.py``
====================

With a new place to send the changes, I needed to change my custom
handler -- the callable instance we registered with the custom
directive -- to send over the changeset information, instead of
just logging it.

View and Template
=================

With the changes now being stored on the site root, I changed the
view to extract it and the template to render it.

Some Refactoring
================

Stuff wasn't in the "right" place. I had type hinting defined in the
sample application, so moved it to place the originates it -- the
threadrunner which sends changes to the callback.

I defined a dataclass ``ChangeSet`` to represent a timestamp and a set of
``ChangeSetEntry`` items. A ``ChangeSetEntry`` is the enum for the kind
of change and a string for the path. (Later, hopefully, a ``Path``.)

I then changed ``threadrunner`` to make an instance of ``ChangeSet`` and
pass it to the callback.

With proper "ChangeSet", I modified the Jinja2 template to display the
timestamp. I also put the type annotations on the intermediate handlers,
to make it clear what is being passed around.