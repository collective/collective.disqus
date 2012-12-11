*****************
collective.disqus
*****************

.. contents:: Table of Contents

Overview
--------

Integrates the `Disqus`_ commenting platform into Plone.

Default Plone discussion mechanism doesn't have a nice panel to administer
comments. It's hard to find new comments. It's not possible to block posts
with links or any other unwelcome contents.

However there are much more specialized tools for commenting on the web:

* `Disqus`_
* `IntenseDebate`_
* `JS-Kit`_

These commenting platforms can be easily integrated with sites, users just
need to create an account and add some special code into their websites.

.. WARNING:: 
   Versions 2.0 and up are not backwards compatible. If you are coming from an
   old version, you'll need to write your own upgrade code, or simply
   manually uninstall the old package before installing the new one.

Configuration
-------------

To enable Disqus comments in your site you need to:

* Enable Global comments from Plone's default "Discussion settings" tool from
  control panel
* Go to Disqus control panel and enable "Activate Disqus as system comment for
  Plone"
* Enter your blog's short name as provided by Disqus

Now a Disqus comment box should be shown for each content type that has
comments enabled.

Comments count
--------------

The product provides a 'Disqus summary view' that you can apply to any
folderish or collection-type content type. It will show a comments count
next to the "Read more..." link of each element.

In addition, there's a counter beneath the title of any object that accepts
comments. This is done through a viewlet named as "disqus.comments.count".

Portlets
--------

This product provides 2 portlets that you can use:

* `Hot threads`_
* `Popular threads`_

They both use the Disqus API, and for them to work, you need to provide:

* Access token
* Public key
* Secret key

And to get them, you need to register an `API Disqus account`_

Disqus API
----------

More info in http://docs.disqus.com/developers/api/

Mostly Harmless
---------------

.. image:: https://secure.travis-ci.org/collective/collective.disqus.png
    :target: http://travis-ci.org/collective/collective.disqus

Have an idea? Found a bug? Let us know by `opening a support ticket`_.

.. _`opening a support ticket`: https://github.com/collective/collective.disqus/issues
.. _`Disqus`: http://disqus.com/
.. _`IntenseDebate`: http://intensedebate.com/
.. _`JS-Kit`: http://js-kit.com/
.. _`Hot threads`: http://disqus.com/api/docs/threads/listHot/
.. _`Popular threads`: http://disqus.com/api/docs/threads/listPopular/
.. _`API Disqus account`: http://disqus.com/api/docs/
