# -*- coding: utf-8 -*-

from time import time

from zope import schema
from zope.component import getUtility
from zope.formlib import form
from zope.interface import implements

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.memoize import ram

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from collective.prettydate.interfaces import IPrettyDate

from collective.disqus import _
from collective.disqus.config import TCACHE
from collective.disqus.utils import disqus_list_popular


def cache_key_simple(func, var):
    timeout = time() // TCACHE
    return (timeout,
            var.data.header,
            var.data.forum,
            var.data.max_results,
            var.data.interval,
            var.data.pretty_date)


class IPopularThreads(IPortletDataProvider):
    """
    """

    header = schema.TextLine(
        title=_(u'Header'),
        description=_(
            u'The header for the portlet. Leave empty for none.'),
        required=False,
    )

    forum = schema.TextLine(
        title=_(u'Forum'),
        description=_(
            u'Specify the forum you wish to obtain the popular threads from.'),
        required=True,
    )

    max_results = schema.Int(
        title=_(u'Maximum results'),
        description=_(u'The maximum results number.'),
        required=True,
        default=5,
    )

    interval = schema.TextLine(
        title=_(u'Interval'),
        description=_(u'Choices: 1h, 6h, 12h, 1d, 7d, 30d, 90d'),
        required=True,
        default=u'7d',
    )

    pretty_date = schema.Bool(
        title=_(u'Pretty dates'),
        description=_(u'Show dates in a pretty format (ie. "4 hours ago").'),
        default=True,
        required=False,
    )


class Assignment(base.Assignment):
    """ Portlet assignment.
    """

    implements(IPopularThreads)

    forum = u''
    max_results = 5
    header = None
    interval = u'7d'
    pretty_date = True

    def __init__(self,
                 max_results,
                 interval,
                 forum,
                 header=None,
                 pretty_date=True):

        self.forum = forum
        self.max_results = max_results
        self.header = header
        self.interval = interval
        self.pretty_date = pretty_date

    @property
    def title(self):
        """ This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return _(u'Popular Threads')


class Renderer(base.Renderer):
    """ Portlet renderer.
    """

    render = ViewPageTemplateFile('popular_threads.pt')

    def getHeader(self):
        """ Returns the header for the portlet.
        """
        return self.data.header

    @ram.cache(cache_key_simple)
    def getPopularPosts(self):
        """
        """
        return disqus_list_popular(self.data.forum,
                                   self.data.max_results,
                                   self.data.interval)

    def getDate(self, date):
        if self.data.pretty_date:
            # Returns human readable date
            date_utility = getUtility(IPrettyDate)
            date = date_utility.date(date)

        return date


class AddForm(base.AddForm):
    """ Portlet add form.
    """
    form_fields = form.Fields(IPopularThreads)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """ Portlet edit form.
    """
    form_fields = form.Fields(IPopularThreads)
