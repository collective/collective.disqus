from zope.interface import Interface
from zope import schema

from plone.app.discussion.interfaces import IDiscussionLayer

from collective.disqus import _
from collective.disqus import i18n


class IDisqusLayer(IDiscussionLayer):
    """ Layer interface for collective.disqus add-on. """


class IDisqusSettings(Interface):
    """ Disqus service need settings. """

    activated = schema.Bool(
        title=i18n.activated,
        description=_(u''),
    )

    forum_short_name = schema.ASCIILine(
        title=i18n.forum_short_name,
        description=_(u''),
    )

    access_token = schema.TextLine(
        title=_(u'Access Token'),
        description=_(u'Access token to retrieve information from the Disqus forum.'),
        required=True,
    )

    app_public_key = schema.TextLine(
        title=_(u'Application public key'),
        description=_(u'public key'),
        required=True,
    )

    app_secret_key = schema.TextLine(
        title=_(u'Application secret key'),
        description=_(u'secret key'),
        required=True,
    )
