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

    developer_mode = schema.Bool(
        title=i18n.developer_mode,
        description=_(u'Mark this box to use Disqus in developer mode.'),
    )

    forum_short_name = schema.ASCIILine(
        title=i18n.forum_short_name,
        description=_(u''),
    )

    extra_forum_short_names = schema.List(
        title=_(u'Additional forum shortnames'),
        description=_(u'Use this option if your site contains several '
                      u'subsections (subsites) and you want to use different '
                      u'Disqus forums for them, or if you want to have '
                      u'different moderators for different parts of it.'),
        default=[],
        value_type=schema.TextLine(
            title=_(u'The forum shortname as registered on Disqus.'),
        ),
        required=False,
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
