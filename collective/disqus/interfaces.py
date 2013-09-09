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
        description=_(u'Mark this box to use Disqus in developer mode'),
    )

    forum_short_name = schema.ASCIILine(
        title=i18n.forum_short_name,
        description=_(u''),
    )

    extra_forum_short_names = schema.List(
        title=u'Website short names (additional)',
        description=u'The single Plone site can have different '
                     'Discus short names for different sections '
                     'so you can migrate the specific subsite '
                     'to different domain/url, etc. Using this option '
                     'you might have different moderators for different '
                     'Plone site sections. '
                     'Please specify a string in the following '
                     'format -  subsite : a forum id. '
                     'E.g.: blogs/test : test',
        default=[],
        value_type=schema.TextLine(title=u'This short name is used to uniquely '
                                         u'identify your subsite on DISQUS.'),
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
