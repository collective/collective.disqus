# -*- coding: utf-8 -*-
from collective.disqus import _
from collective.disqus import i18n
from plone.app.discussion.interfaces import IDiscussionLayer
from zope import schema
from zope.interface import Interface


class IDisqusLayer(IDiscussionLayer):
    """ Layer interface for collective.disqus add-on. """


class IDisqusSettings(Interface):
    """ Disqus service need settings. """

    activated = schema.Bool(
        title=i18n.activated,
        description=_(u''),
    )

    developer_mode = schema.Bool(
        title=i18n.developer_mode,
        description=_(u'Mark this box to use Disqus in developer mode'),
    )

    forum_short_name = schema.ASCIILine(
        title=i18n.forum_short_name,
        description=_(u''),
    )

    access_token = schema.TextLine(
        title=_(u'Access Token'),
        description=_(u'Access token to retrieve information from the Disqus forum.'),
        required=False,
    )

    app_public_key = schema.TextLine(
        title=_(u'Application public key'),
        description=_(u'public key'),
        required=False,
    )

    app_secret_key = schema.TextLine(
        title=_(u'Application secret key'),
        description=_(u'secret key'),
        required=False,
    )
