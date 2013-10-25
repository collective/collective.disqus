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

Installation
------------

To enable this package in a buildout-based installation:

1. Edit your buildout.cfg and add ``collective.disqus`` to the list of eggs to
   install::

    [buildout]
    ...
    eggs =
        collective.disqus

After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``collective.disqus`` and click the 'Activate' button.

.. Note::
	You may have to empty your browser cache and save your resource registries
	in order to see the effects of the product installation.

Upgrading from 0.3.1
^^^^^^^^^^^^^^^^^^^^

.. Warning::
   Versions 2.0 and up are not backwards compatible. If you are coming from an
   old version, you'll need to write your own upgrade code, or simply manually
   uninstall the old package before installing the new one.

If you're upgrading from a pre-2.0 installation you'll have to manually 
reconfigure the @@disqus-controlpanel.

A GenericSetup upgrade profile called "collective.disqus: cleanup old 0.3.1
install" will undo the viewlet suppression that was part of 0.3.1. This may
also unhide other belowcontent viewlets, YMMV. It does not provide a full
upgrade.

Usage
-----

Configuration
^^^^^^^^^^^^^

To enable Disqus comments in your site you need to:

* Enable Global comments from Plone's default "Discussion settings" tool from
  control panel
* Go to Disqus control panel and enable "Activate Disqus as system comment for
  Plone"
* Enter your blog's short name as provided by Disqus

Now a Disqus comment box should be shown for each content type that has
comments enabled.

Comments count
^^^^^^^^^^^^^^

The product provides a 'Disqus summary view' that you can apply to any
folderish or collection-type content type. It will show a comments count
next to the "Read more..." link of each element.

In addition, there's a counter beneath the title of any object that accepts
comments. This is done through a viewlet named as "disqus.comments.count".

Portlets
^^^^^^^^

This product provides 2 portlets that you can use:

* `Hot threads`_: Shows a list of threads sorted by hotness (date and likes)

* `Popular threads`_: Shows a list of threads sorted by number of posts made
  since the specified interval

They both use the `Disqus API`_, and for them to work, you need to provide:

* Access token
* Public key
* Secret key

And to get them, you need to register an `API Disqus account`_

Subsites
^^^^^^^^

When website contains several subsections (subsites) and there is a need to
migrate the specific subsite to different domain/url, etc, Disqus offers
options only for whole "shortnames" but not for specific pages/documents. With
the addition of ability to have multiple configurable shortnames, a single
Plone site can now have different Disqus "shortnames" for different sections.

Another possible scenario is the requirement to have different moderators for
different Plone site sections. This is achieved only by different Disqus
"shortnames".

To use this option, enter your blogs's/subsite's short names into the
'Additional forum shortnames' field.

TODO
^^^^

Add a portlet that shows a list of `Trending threads`_.

Mostly Harmless
---------------

.. image:: https://secure.travis-ci.org/collective/collective.disqus.png?branch=master
    :target: http://travis-ci.org/collective/collective.disqus

.. image:: https://coveralls.io/repos/collective/collective.disqus/badge.png?branch=master
    :target: https://coveralls.io/r/collective/collective.disqus

Got an idea? Found a bug? Let us know by `opening a support ticket`_.

.. _`API Disqus account`: http://disqus.com/api/docs/
.. _`Disqus API`: http://docs.disqus.com/developers/api/
.. _`Disqus`: http://disqus.com/
.. _`Hot threads`: http://disqus.com/api/docs/threads/listHot/
.. _`IntenseDebate`: http://intensedebate.com/
.. _`JS-Kit`: http://js-kit.com/
.. _`opening a support ticket`: https://github.com/collective/collective.disqus/issues
.. _`Popular threads`: http://disqus.com/api/docs/threads/listPopular/
.. _`Trending threads`: http://disqus.com/api/docs/trends/listThreads/
