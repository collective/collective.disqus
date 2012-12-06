*****************
collective.disqus
*****************

.. contents:: Table of Contents

Overview
--------

Integrates the `Disqus`_ commenting platform in Plone.

Default Plone discussion mechanism doesn't have nice panel to administer
comments. It's hard to find new comments. It's not possible to block posts
with links or some other unwelcome contents.

But on the web there are much more specialized tools for commenting:

- `Disqus`_
- `IntenseDebate`_
- `JS-Kit`_

These commenting platforms can be easyly integrated with sites, users just
need to create an account and add some special code into their websites.

Configuration
-------------

Go to Site Setup -> `Disqus`_ comment system control panel form and configure
website short name. `Disqus`_ should be visible in all contents that enabled
commenting.

Disqus API
----------

More info in http://docs.disqus.com/developers/api/

Comments count
--------------

The product provides a 'Disqus summary view' that you can apply to any 
folderish or collection-type content type. It will show a comments count 
next to the "Read more..." link of each element.

In addition, there's a counter beneath the title of any object that
accepts comments. This is done through a viewlet.

The viewlet's name is "disqus.comments.count"


Mostly Harmless
---------------

.. image:: https://secure.travis-ci.org/collective/collective.disqus.png
    :target: http://travis-ci.org/collective/collective.disqus

Have an idea? Found a bug? Let us know by `opening a support ticket`_.

.. _`opening a support ticket`: https://github.com/collective/collective.disqus/issues
.. _`Disqus`: http://disqus.com/
.. _`IntenseDebate`: http://intensedebate.com/
.. _`JS-Kit`: http://js-kit.com/
