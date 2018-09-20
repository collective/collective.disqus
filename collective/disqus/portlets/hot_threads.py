# -*- coding: utf-8 -*-
from collective.disqus import _
from collective.disqus.config import IS_PLONE_5
from collective.disqus.config import TCACHE
from collective.disqus.utils import disqus_list_hot
from collective.prettydate.interfaces import IPrettyDate
from plone.app.portlets.portlets import base
from plone.memoize import ram
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from time import time
from zope import schema
from zope.component import getUtility
from zope.interface import implementer


if not IS_PLONE_5:  # BBB
    from zope.formlib import form


def cache_key_simple(func, var):
    timeout = time() // TCACHE
    return (timeout,
            var.data.header,
            var.data.forum,
            var.data.max_results,
            var.data.pretty_date)


class IHotThreads(IPortletDataProvider):
    """A portlet that lists hot threads."""

    header = schema.TextLine(
        title=_(u'Header'),
        description=_(u'The header for the portlet. Leave empty for none.'),
        required=False,
    )

    forum = schema.TextLine(
        title=_(u'Forum'),
        description=_(
            u'Specify the forum you wish to obtain the hot threads from.'),
        required=True,
    )

    max_results = schema.Int(
        title=_(u'Maximum results'),
        description=_(u'The maximum results number.'),
        required=True,
        default=5,
    )

    pretty_date = schema.Bool(
        title=_(u'Pretty dates'),
        description=_(u'Show dates in a pretty format (ie. "4 hours ago").'),
        default=True,
        required=False,
    )


@implementer(IHotThreads)
class Assignment(base.Assignment):
    """Portlet assignment."""

    forum = u''
    max_results = 5
    header = None
    pretty_date = True

    def __init__(self,
                 max_results,
                 forum,
                 header=None,
                 pretty_date=True):

        self.forum = forum
        self.max_results = max_results
        self.header = header
        self.pretty_date = pretty_date

    @property
    def title(self):
        """Return title of the portlet in the "manage portlets" screen."""
        return _(u'Hot Threads')


class Renderer(base.Renderer):
    """Portlet renderer."""

    render = ViewPageTemplateFile('hot_threads.pt')

    def getHeader(self):
        """Returns the header for the portlet."""
        return self.data.header

    @ram.cache(cache_key_simple)
    def getPopularPosts(self):
        return disqus_list_hot(self.data.forum, self.data.max_results)

    def getDate(self, date):
        if self.data.pretty_date:
            # Returns human readable date
            date_utility = getUtility(IPrettyDate)
            date = date_utility.date(date)

        return date


class AddForm(base.AddForm):
    """Portlet add form."""
    if IS_PLONE_5:
        schema = IHotThreads
    else:  # BBB
        form_fields = form.Fields(IHotThreads)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form."""
    if IS_PLONE_5:
        schema = IHotThreads
    else:  # BBB
        form_fields = form.Fields(IHotThreads)
