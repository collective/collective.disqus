from collective.disqus import i18n
from plone.app.discussion.interfaces import IDiscussionLayer
from zope import interface
from zope import schema

class IDisqusLayer(IDiscussionLayer):
    """Layer interface for collective.disqus add-on"""

class IDisqusSettings(interface.Interface):
    """Disqus service need settings"""
    
    activated = schema.Bool(title=i18n.activated)
    
    forum_short_name = schema.ASCIILine(title=i18n.forum_short_name)
